#!/usr/bin/env python3
"""Fetch consolidated (current) texts of Czech legislation from e-Sbírka.

1. Downloads the official open-data metadata dump (006PravniAktMetadata.json.gz)
   from https://opendata.eselpoint.gov.cz/datove-sady-esbirka/ and selects every
   act of the Collection of Laws (Sbírka zákonů, "sb") of the selected kinds that has
   no repeal date (datum zrušení / platnosti do).
2. For each selected act, calls the public e-Sbírka REST API used by the
   e-sbirka.gov.cz web application:
     GET https://e-sbirka.gov.cz/sbr-cache/dokumenty-sbirky/{staleUrl}
     GET https://e-sbirka.gov.cz/sbr-cache/dokumenty-sbirky/{staleUrl}/fragmenty?cisloStranky=N
   and stores the document detail + all fragments as gzipped JSON under
   RAW/api/<year>/<number>.json.gz (cache: existing files are skipped).

Usage: python fetch.py [--raw DIR] [--workers 3] [--limit N] [--only 1/1993,2/1993]
"""
import argparse
import gzip
import json
import os
import sys
import threading
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
OPENDATA = "https://opendata.eselpoint.gov.cz/datove-sady-esbirka/"
API = "https://e-sbirka.gov.cz/sbr-cache/dokumenty-sbirky/"

# druh aktu (kind) -> category directory
KINDS = {
    "ZAKONUST": "ustavni-zakony",
    "ZAKON": "zakony",
    "NARIZVLA": "narizeni-vlady",
    "VYHLASKA": "vyhlasky",
    "VYHLASVL": "vyhlasky",
    "DEKRETUST": "dekrety",
    "DEKRET": "dekrety",
    "OPATRZAK": "zakonna-opatreni",
    "OPATRSEN": "zakonna-opatreni",
    "NARIZENI": "narizeni",
}

_local = threading.local()


def session():
    s = getattr(_local, "s", None)
    if s is None:
        s = requests.Session()
        s.headers["User-Agent"] = UA
        s.headers["Accept"] = "application/json"
        _local.s = s
    return s


def get(url, stream=False, tries=6):
    delay = 5
    for i in range(tries):
        try:
            r = session().get(url, timeout=180, stream=stream)
            if r.status_code == 200:
                return r
            if r.status_code in (404, 400):
                return r
            print(f"HTTP {r.status_code} {url}", file=sys.stderr)
        except requests.RequestException as e:
            print(f"ERR {e} {url}", file=sys.stderr)
        time.sleep(delay)
        delay = min(delay * 2, 120)
    raise RuntimeError(f"giving up on {url}")


def download(name, raw):
    path = os.path.join(raw, "dl", name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        return path
    r = get(OPENDATA + name, stream=True)
    tmp = path + ".part"
    with open(tmp, "wb") as f:
        for chunk in r.iter_content(1 << 20):
            f.write(chunk)
    with gzip.open(tmp) as g:  # integrity check
        while g.read(1 << 24):
            pass
    os.replace(tmp, path)
    return path


def select(raw):
    meta = json.load(gzip.open(download("006PravniAktMetadata.json.gz", raw)))["položky"]
    # the dump holds several metadata records per act (one per metadata version):
    # keep only the latest (highest metadata-id) record of each act
    latest = {}
    for m in meta:
        k = m["akt-iri"]
        if k not in latest or m["metadata-id"] > latest[k]["metadata-id"]:
            latest[k] = m
    out = []
    for m in latest.values():
        parts = m["akt-iri"].split("/")  # esel-esb:eli/cz/sb/1993/1
        if parts[2] != "sb":
            continue
        if m["cis-esb-typ-právní-akt-položka"] != "PRAVPRED":
            continue
        kind = m["cis-esb-druh-aktu-položka"]
        sub = m["cis-esb-podtyp-právní-akt-položka"]
        if kind == "USNESENI" and sub == "ZAKONUST":
            kind = "ZAKONUST"  # 2/1993 Sb. Listina základních práv a svobod
        if kind == "OPATRENI" and sub == "OPATRSEN":
            kind = "OPATRSEN"
        if kind not in KINDS:
            continue
        if m["metadata-datum-zrušení"] or m["metadata-datum-platnosti-do"]:
            continue
        out.append({
            "year": int(parts[3]), "number": parts[4], "kind": kind, "subtype": sub,
            "citation": m["akt-citace"], "title": m["metadata-název"],
            "short_title": m["metadata-název-zkrácený"],
            "approved": m["metadata-datum-schválení"],
            "effective": m["metadata-datum-účinnosti-od"],
            "eli": m["metadata-eli"],
        })
    out.sort(key=lambda x: (x["year"], int(x["number"]) if x["number"].isdigit() else 0, x["number"]))
    with open(os.path.join(raw, "selection.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=0)
    return out


def fetch_one(item, raw):
    path = os.path.join(raw, "api", str(item["year"]), f"{item['number']}.json.gz")
    if os.path.exists(path):
        return "cached"
    stale = f"/sb/{item['year']}/{item['number']}"
    r = get(API + urllib.parse.quote(stale, safe=""))
    if r.status_code != 200:
        return f"detail {r.status_code}"
    detail = r.json()
    stale = detail.get("staleUrl") or stale
    q = urllib.parse.quote(stale, safe="")
    frags = []
    page, pages = 0, 1
    while page < pages:
        r = get(f"{API}{q}/fragmenty?cisloStranky={page}")
        if r.status_code != 200:
            return f"fragments {r.status_code}"
        d = r.json()
        pages = d.get("pocetStranek", 1)
        frags.extend(d.get("seznam", []))
        page += 1
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = f"{path}.{os.getpid()}.{threading.get_ident()}.part"
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        json.dump({"item": item, "detail": detail, "fragments": frags}, f, ensure_ascii=False)
    os.replace(tmp, path)
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=os.path.join(os.path.dirname(__file__), "..", "..", "_raw", "cz"))
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--only")
    a = ap.parse_args()
    raw = os.path.abspath(a.raw)
    items = select(raw)
    if a.only:
        want = set(a.only.split(","))
        items = [i for i in items if f"{i['number']}/{i['year']}" in want]
    if a.limit:
        items = items[: a.limit]
    print(f"{len(items)} acts selected", flush=True)
    done = 0
    with ThreadPoolExecutor(a.workers) as ex:
        futs = {ex.submit(fetch_one, i, raw): i for i in items}
        for fu in as_completed(futs):
            i = futs[fu]
            done += 1
            try:
                res = fu.result()
            except Exception as e:  # noqa
                res = f"FAIL {e}"
            if res not in ("ok", "cached"):
                print(f"{i['citation']}: {res}", flush=True)
            if done % 200 == 0:
                print(f"{done}/{len(items)}", flush=True)


if __name__ == "__main__":
    main()
