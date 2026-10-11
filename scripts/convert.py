#!/usr/bin/env python3
"""Convert e-Sbírka API JSON (cached by fetch.py) to LawCodex Markdown.

Usage: python convert.py [--raw DIR] [--out REPO_DIR] [--retrieved YYYY-MM-DD]
"""
import argparse
import datetime
import glob
import gzip
import html
import json
import os
import re
import sys
import unicodedata

from lxml import html as lhtml

SITE = "https://e-sbirka.gov.cz"
FILES = SITE + "/sbr-externi/souborove-dokumenty/{id}/{kind}/{op}/{name}"

TYPE = {
    "ZAKONUST": "constitutional_act",
    "ZAKON": "act",
    "NARIZVLA": "government_regulation",
    "VYHLASKA": "decree",
    "VYHLASVL": "decree",
    "DEKRETUST": "constitutional_decree",
    "DEKRET": "decree_of_the_president",
    "OPATRZAK": "legislative_measure",
    "OPATRSEN": "legislative_measure",
    "NARIZENI": "regulation",
}
DIRS = {
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
BY_YEAR = {"zakony", "narizeni-vlady", "vyhlasky"}
CONSTITUTION = {("1993", "1"), ("1993", "2")}

# Fragment types rendered as headings (structural units)
HEADINGS = {
    "Cast", "Hlava", "Dil", "Oddil", "Pododdil", "Kapitola", "Clanek", "ClanekMS", "Paragraf",
    "Priloha", "Hlavicka_priloha", "Nazev_Priloha", "Cast_Priloha", "Nadpis",
    "Sekce_Obecna", "Sekce_Zvlastni", "Clanek_novely",
}
SKIP = {
    "Block_Komentare", "Block_Jeden_Komentar", "Block_Pripominky", "Block_Jedna_Pripominka",
    "Block_PN", "Block_Jeden_PN", "Block_Oduvodneni_Pripominek", "Block_Jedno_Oduvodneni",
    "Virtual_Skryta",
}


def slugify(s, maxlen=70):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rsplit("-", 1)[0]
    return s


def esc(t):
    """Escape Markdown-significant characters in a text node."""
    t = t.replace("\\", "\\\\").replace("*", "\\*").replace("`", "\\`")
    t = t.replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"(?<![0-9A-Za-zÀ-ž])_|_(?![0-9A-Za-zÀ-ž])", r"\\_", t)
    t = t.replace("](", "]\\(")
    return t


def norm_ws(s):
    s = s.replace("\u00a0", " ")
    return re.sub(r"[ \t\r\n]+", " ", s)


def file_url(fid, name, kind="NAHLED", op="ZOBRAZ"):
    return FILES.format(id=fid, kind=kind, op=op, name=name)


def _lname(el):
    return el.tag.split("}")[-1].lower() if isinstance(el.tag, str) else ""


def math_html(el):
    """Render a (simple) MathML subtree as text with <sub>/<sup>."""
    name = _lname(el)
    kids = [k for k in el if isinstance(k.tag, str)]
    if name in ("mi", "mn", "mo", "mtext", "ms"):
        return esc(norm_ws(el.text_content()))
    if name == "none" or name == "mprescripts":
        return ""
    if name == "msup" and len(kids) == 2:
        return math_html(kids[0]) + f"<sup>{math_html(kids[1])}</sup>"
    if name == "msub" and len(kids) == 2:
        return math_html(kids[0]) + f"<sub>{math_html(kids[1])}</sub>"
    if name == "msubsup" and len(kids) == 3:
        return math_html(kids[0]) + f"<sub>{math_html(kids[1])}</sub><sup>{math_html(kids[2])}</sup>"
    if name == "mfrac" and len(kids) == 2:
        return f"({math_html(kids[0])})/({math_html(kids[1])})"
    if name == "msqrt":
        return "√(" + "".join(math_html(k) for k in kids) + ")"
    if name == "mmultiscripts" and kids:
        base, rest = kids[0], kids[1:]
        names = [_lname(k) for k in rest]
        if "mprescripts" in names:
            i = names.index("mprescripts")
            post, pre = rest[:i], rest[i + 1:]
        else:
            post, pre = rest, []
        def scripts(lst):
            o = ""
            for j in range(0, len(lst) - 1, 2):
                sb, sp = math_html(lst[j]), math_html(lst[j + 1])
                o += (f"<sub>{sb}</sub>" if sb else "") + (f"<sup>{sp}</sup>" if sp else "")
            return o
        return scripts(pre) + math_html(base) + scripts(post)
    return "".join(math_html(k) for k in kids) if kids else esc(norm_ws(el.text_content()))


class Ctx:
    def __init__(self, files):
        self.files = {f["souborovyDokumentId"]: f for f in files or []}
        self.used = set()


def inline(el, ctx, in_table=False):
    out = []
    if el.text:
        out.append(esc(norm_ws(el.text)))
    for ch in el:
        tag = ch.tag if isinstance(ch.tag, str) else ""
        tag = tag.lower()
        if tag == "math" or tag.endswith("}math"):
            out.append(math_html(ch))
        elif tag == "br":
            out.append("<br>" if in_table else "  \n")
        elif tag in ("sup", "sub"):
            out.append(f"<{tag}>{inline(ch, ctx, in_table).strip()}</{tag}>")
        elif tag in ("b", "strong"):
            inner = inline(ch, ctx, in_table).strip()
            m = re.match(r"^(.*?)((?:\s|<br>)*)$", inner, re.S)
            inner, trail = m.group(1), m.group(2)
            out.append((f"**{inner}**" if inner else "") + trail)
        elif tag in ("i", "em"):
            inner = inline(ch, ctx, in_table).strip()
            m = re.match(r"^(.*?)((?:\s|<br>)*)$", inner, re.S)
            inner, trail = m.group(1), m.group(2)
            out.append((f"*{inner}*" if inner else "") + trail)
        elif tag == "img":
            fid = ch.get("data-souborovy-dokument-id")
            alt = ch.get("alt") or ""
            if fid and fid.isdigit():
                ctx.used.add(int(fid))
                info = ctx.files.get(int(fid))
                name = (info or {}).get("nazev") or re.sub(r"\.tif$", "", alt, flags=re.I) or "obrazek"
                out.append(f"![{esc(alt)}]({file_url(fid, name)})")
            elif ch.get("src", "").startswith("http"):
                out.append(f"![{esc(alt)}]({ch.get('src')})")
        elif tag == "table":
            out.append("\n\n" + table(ch, ctx) + "\n\n")
        elif tag in ("p", "div", "li", "tr"):
            out.append("\n\n" + inline(ch, ctx, in_table).strip() + "\n\n")
        elif tag in ("script", "style"):
            pass
        else:  # var, a, span, czechvoc-termin, u, ... -> text content
            out.append(inline(ch, ctx, in_table))
        if ch.tail:
            out.append(esc(norm_ws(ch.tail)))
    return "".join(out)


def cell_text(c, ctx):
    t = inline(c, ctx, in_table=True)
    t = re.sub(r"\s*\n\s*\n\s*", "<br>", t.strip())
    return t.replace("|", "\\|").replace("\n", " ").strip()


def table(t, ctx):
    rows = t.xpath(".//tr")
    simple = rows and not t.xpath(".//table") and not t.xpath(".//*[@rowspan>1 or @colspan>1]")
    if simple:
        grid = [[cell_text(c, ctx) for c in r if isinstance(c.tag, str) and c.tag.lower() in ("td", "th")] for r in rows]
        grid = [g for g in grid if g]
        if grid:
            n = max(len(g) for g in grid)
            grid = [g + [""] * (n - len(g)) for g in grid]
            lines = ["| " + " | ".join(grid[0]) + " |", "|" + "---|" * n]
            lines += ["| " + " | ".join(g) + " |" for g in grid[1:]]
            return "\n".join(lines)
    # complex table: clean HTML
    for img in t.xpath(".//img"):
        fid = img.get("data-souborovy-dokument-id")
        alt = img.get("alt") or ""
        if fid and fid.isdigit():
            ctx.used.add(int(fid))
            info = ctx.files.get(int(fid))
            name = (info or {}).get("nazev") or re.sub(r"\.tif$", "", alt, flags=re.I) or "obrazek"
            img.set("src", file_url(fid, name))
    for m in t.xpath(".//*[local-name()='math']"):
        repl = lhtml.fragment_fromstring("<span>" + math_html(m) + "</span>")
        repl.tail = m.tail
        m.getparent().replace(m, repl)
    for el in t.iter():
        if not isinstance(el.tag, str):
            continue
        keep = ("rowspan", "colspan", "src", "alt") if el.tag == "img" else ("rowspan", "colspan")
        for a in list(el.attrib):
            if a not in keep:
                del el.attrib[a]
    for el in t.xpath(".//var|.//a|.//czechvoc-termin|.//span"):
        el.drop_tag()
    s = lhtml.tostring(t, encoding="unicode")
    s = re.sub(r">\s+<", "><", s)
    return s.strip()


def render_xhtml(x, ctx):
    if not x:
        return ""
    try:
        root = lhtml.fragment_fromstring(x, create_parent="div")
    except Exception:  # noqa
        return esc(norm_ws(html.unescape(re.sub(r"<[^>]+>", " ", x))))
    s = inline(root, ctx)
    s = re.sub(r"[ \t]*\n[ \t]*\n\s*", "\n\n", s)
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


def block_escape(s):
    """Prevent paragraph starts being read as lists / headings / quotes."""
    out = []
    for line in s.split("\n"):
        m = re.match(r"^(\s*)(\d+)([.)])(\s)", line)
        if re.match(r"^\|.*\|$", line) or line.startswith("<table"):
            pass
        elif m:
            line = m.group(1) + m.group(2) + "\\" + m.group(3) + line[m.end(3):]
        elif re.match(r"^\s*([-+#>=]|\|)", line) and not line.lstrip().startswith("| ") and not line.lstrip().startswith("<"):
            line = re.sub(r"^(\s*)", r"\1\\", line, count=1)
        out.append(line)
    return "\n".join(out)


def plain(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("\\", "")
    return norm_ws(html.unescape(s)).strip()


def convert_doc(d):
    item, detail, frags = d["item"], d["detail"], d["fragments"]
    body = []
    pending_heading = None  # (level, text, hloubka, quoted)
    quote = []  # stack of Block_Citace depths (quoted text inside amending provisions)

    def emit(block, quoted):
        if quoted:
            block = "\n".join(("> " + ln) if ln.strip() else ">" for ln in block.split("\n"))
        body.append(block)

    def flush():
        nonlocal pending_heading
        if pending_heading:
            lvl, txt, _, q = pending_heading
            if lvl <= 6 and not q:
                emit("#" * lvl + " " + txt, q)
            else:
                emit(f"**{txt}**", q)
            pending_heading = None

    skip_depth = None
    for f in frags:
        t = f["kodTypuFragmentu"]
        depth = f.get("hloubka", 0)
        if skip_depth is not None:
            if depth > skip_depth:
                continue
            skip_depth = None
        while quote and depth <= quote[-1]:
            quote.pop()
        if t in SKIP:
            skip_depth = depth
            continue
        if t in ("Block_Citace", "Eu_Block_Citace"):
            quote.append(depth)
        q = bool(quote)
        ctx = Ctx(f.get("souboroveDokumenty"))
        x = f.get("xhtml") or ""
        text = render_xhtml(x, ctx)
        extra = []
        for fid, info in ctx.files.items():
            if fid not in ctx.used:
                name = info.get("nazev") or str(fid)
                extra.append(f"[{esc(name)}]({file_url(fid, name, 'ORIGINAL', 'STAHNI')})")
        if t.startswith("Virtual_"):
            if t == "Virtual_PPC":
                flush()
                body.append("---")
            continue
        if not text and not extra:
            continue
        if t in HEADINGS or t == "Nadpis_pod":
            text = re.sub(r"(?<!\\)\*\*", "", text).strip() if "\n" not in text else text
        if t in HEADINGS and text and "\n" not in text and len(text) < 300:
            flush()
            pending_heading = (max(2, min(depth, 7)), text, depth, q)
            if extra:
                flush()
                emit(block_escape("  \n".join(extra)), q)
            continue
        if (t == "Nadpis_pod" and pending_heading and depth == pending_heading[2] + 1
                and "\n" not in text and pending_heading[3] == q):
            lvl, txt, hd, _ = pending_heading
            pending_heading = (lvl, f"{txt} – {text}", hd, q)
            continue
        flush()
        if t in ("Nadpis_nad", "Nadpis_pod", "Nadpis_pod_velkymi") and "\n" not in text:
            emit(f"**{text}**", q)
        else:
            if text:
                emit(block_escape(text), q)
            if extra:
                emit("  \n".join(extra), q)
    flush()
    return "\n\n".join(body)


def yq(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def target_path(item, detail):
    y, n = str(item["year"]), item["number"]
    name_src = item.get("short_title") or detail.get("nazev") or item["title"]
    # strip leading kind word ("Zákon", "Vyhláška", ...) from the title for the slug
    cit = detail.get("uplnaCitace") or ""
    if ", " in cit:
        name_src = cit.split(", ", 1)[1]
    slug = slugify(name_src)
    fname = f"{n}-{y}" + (f"-{slug}" if slug else "") + ".md"
    if (y, n) == ("1993", "2"):
        fname = "2-1993-listina-zakladnich-prav-a-svobod.md"
    if (y, n) in CONSTITUTION:
        return os.path.join("ustava", fname)
    d = DIRS[item["kind"]]
    if d in BY_YEAR:
        return os.path.join(d, y, fname)
    return os.path.join(d, fname)


def render(d, retrieved):
    item, detail = d["item"], d["detail"]
    title = detail.get("uplnaCitace") or item["title"]
    title = norm_ws(title).strip()
    kind = item["kind"]
    typ = TYPE[kind]
    if (str(item["year"]), item["number"]) == ("1993", "1"):
        typ = "constitution"
    elif (str(item["year"]), item["number"]) == ("1993", "2"):
        typ = "charter_of_fundamental_rights"
    fm = ["---", f"title: {yq(title)}", f"identifier: {yq(item['citation'])}"]
    eli = detail.get("eli") or item.get("eli")
    if eli:
        fm.append(f"eli: {yq('https://e-sbirka.gov.cz' + eli if eli.startswith('/') else eli)}")
    fm += [f"type: {typ}", "jurisdiction: cz", "language: cs"]
    if item.get("approved"):
        fm.append(f"date: {item['approved']}")
    if detail.get("datumUcinnostiOd") or item.get("effective"):
        fm.append(f"effective: {detail.get('datumUcinnostiOd') or item.get('effective')}")
    if detail.get("datumUcinnostiZneniOd"):
        fm.append(f"last_amended: {detail['datumUcinnostiZneniOd']}")
    fm.append("status: in_force")
    fm.append(f"source: {yq(SITE + '/sb/' + str(item['year']) + '/' + item['number'])}")
    fm.append(f"retrieved: {retrieved}")
    if detail.get("uplnaCitaceSNovelami") and detail["uplnaCitaceSNovelami"] != title:
        fm.append(f"citation_with_amendments: {yq(norm_ws(detail['uplnaCitaceSNovelami']).strip())}")
    fm.append("---")
    body = convert_doc(d)
    h1 = title
    if (str(item["year"]), item["number"]) == ("1993", "1"):
        h1 = detail.get("nazev") or title
    elif (str(item["year"]), item["number"]) == ("1993", "2"):
        h1 = "Listina základních práv a svobod"
    return "\n".join(fm) + "\n\n# " + esc(h1) + "\n\n" + body + "\n"


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--raw", default=os.path.join(here, "..", "..", "_raw", "cz"))
    ap.add_argument("--out", default=os.path.join(here, ".."))
    ap.add_argument("--retrieved", default=datetime.date.today().isoformat())
    ap.add_argument("--clean", action="store_true", help="remove generated category dirs first")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    files = a.files or sorted(glob.glob(os.path.join(a.raw, "api", "*", "*.json.gz")))
    selected = None
    sel_path = os.path.join(a.raw, "selection.json")
    if os.path.exists(sel_path):
        sel_items = {(str(x["year"]), x["number"]): x for x in json.load(open(sel_path))}
        selected = set(sel_items)
    if a.clean and not a.files:
        import shutil
        for dname in set(DIRS.values()) | {"ustava"}:
            shutil.rmtree(os.path.join(a.out, dname), ignore_errors=True)
    n = 0
    stats = {}
    for p in files:
        try:
            d = json.load(gzip.open(p))
        except Exception as e:  # noqa
            print(f"BAD {p}: {e}", file=sys.stderr)
            continue
        key = (str(d["item"]["year"]), d["item"]["number"])
        if selected is not None and key not in selected:
            continue  # no longer in force according to the latest metadata
        d["item"] = sel_items.get(key, d["item"]) if selected is not None else d["item"]
        if not d.get("fragments"):
            print(f"EMPTY {p}", file=sys.stderr)
            continue
        rel = target_path(d["item"], d["detail"])
        out = os.path.join(a.out, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(render(d, a.retrieved))
        top = rel.split(os.sep)[0]
        stats[top] = stats.get(top, 0) + 1
        n += 1
    print(n, stats)


if __name__ == "__main__":
    main()
