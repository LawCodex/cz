# Czechia — legislation as Markdown (LawCodex)

Consolidated texts (*úplné znění*, the current version in force) of Czech legislation published
in the **Sbírka zákonů** (Collection of Laws), converted to Markdown, one file per act.
Source: the official electronic Collection of Laws **e-Sbírka** (https://e-sbirka.gov.cz),
operated by the Ministry of the Interior of the Czech Republic.

Retrieved: **2026-10-11** (consolidation dates per act are in each file's `last_amended`).

## Coverage

All acts of the Sbírka zákonů (1918–2026) of the kinds below that are **not repealed**
according to the latest e-Sbírka metadata record (no *datum zrušení* / *platnost do*):

| Directory | Contents | Files |
|---|---|---:|
| `ustava/` | Ústava České republiky (1/1993 Sb.) and Listina základních práv a svobod (2/1993 Sb.) | 2 |
| `ustavni-zakony/` | other constitutional acts (*ústavní zákony*), incl. pre-1993 ones still formally valid | 50 |
| `zakony/<year>/` | acts (*zákony*), incl. codes (občanský zákoník 89/2012, trestní zákoník 40/2009, zákoník práce 262/2006, OSŘ 99/1963, …) | 3,182 |
| `narizeni-vlady/<year>/` | government regulations (*nařízení vlády*) | 1,441 |
| `vyhlasky/<year>/` | decrees (*vyhlášky*) of ministries and other central authorities published in the Sbírka zákonů | 4,146 |
| `dekrety/` | presidential decrees 1945 (*dekrety prezidenta republiky*, incl. 6 constitutional decrees) | 60 |
| `zakonna-opatreni/` | legislative measures of the Senate / Presidium of the Federal Assembly (*zákonná opatření*) | 40 |
| `narizeni/` | other *nařízení* published in the Sbírka (mostly 1918–1950) | 14 |
| **Total** | | **8,935** |

Notes:

- "Not repealed" follows e-Sbírka's own metadata. About 2,370 of the *zákony* are amending acts
  (*novely*, "kterým se mění …"). In Czech law these are not formally repealed after they take
  effect, so e-Sbírka lists them as valid, and their consolidated text still contains the
  amending provisions (which are rendered as blockquotes). Many old (pre-1989) acts are also
  formally still valid even if obsolete.
- e-Sbírka omits fully repealed provisions (e.g. a repealed `§ 4` is simply absent) in the
  consolidated text; that is preserved as-is.
- Annexes and images: inline images (scanned formulas, signs, forms) are linked to the
  e-Sbírka file service (`https://e-sbirka.gov.cz/sbr-externi/souborove-dokumenty/<id>/…`), not
  copied into the repo. Annexes published only as files (PDF etc.) are linked the same way.

## Not covered

- Repealed or expired acts and historical versions (only the current consolidated version).
- International treaties (*Sbírka mezinárodních smluv*, "sm") and treaties/communications
  published in the Sbírka zákonů (`MEZINAKT`).
- Other Sbírka contents that are not legal regulations (*sdělení*, *oznámení*, *usnesení*,
  Constitutional Court judgments (*nálezy*), *rozhodnutí*, *opatření*, published full texts
  (*úplná znění*), corrections …).
- Regional / municipal legislation and the *Ústřední věstník* / *Úřední list* collections.
- Explanatory reports, commentary, CzechVOC term links and cross-reference links (link
  text is kept as plain text).

## Format

Each file has YAML front matter:

```yaml
title: "Zákon č. 89/2012 Sb., občanský zákoník"   # official citation (úplná citace)
identifier: "89/2012 Sb."                           # number/year in the Sbírka zákonů
eli: "https://e-sbirka.gov.cz/eli/cz/sb/2012/89/2026-01-01"  # ELI of the consolidated version
type: act        # constitution | charter_of_fundamental_rights | constitutional_act | act |
                 # government_regulation | decree | decree_of_the_president |
                 # constitutional_decree | legislative_measure | regulation
jurisdiction: cz
language: cs
date: 2012-02-03          # date of adoption ("ze dne")
effective: 2014-01-01     # original entry into force
last_amended: 2026-01-01  # effective date of the consolidated version
status: in_force
source: "https://e-sbirka.gov.cz/sb/2012/89"
retrieved: 2026-10-11
citation_with_amendments: "… ve znění …"   # when provided by e-Sbírka
```

The body starts with the act's header (number, kind, issuing body, date, title, enacting
formula), then the structure: *část / hlava / díl / oddíl / pododdíl / § or čl.* are mapped to
Markdown headings by their depth in the e-Sbírka document tree (headings deeper than `######`
become bold lines); unit titles (*nadpis*) are appended to the heading (`## ČÁST PRVNÍ – OBECNÁ
ČÁST`), titles above sections are bold lines. Paragraphs, letters and points are plain paragraphs
keeping their labels (`(1)`, `a)`, `1.`). Footnotes (*poznámky pod čarou*) follow a horizontal
rule at the end of the text, followed by signatures and annexes as in e-Sbírka. Simple tables are
Markdown tables; tables with merged cells are kept as HTML; MathML is flattened to text with
`<sub>`/`<sup>`.

File names: `<number>-<year>-<slug>.md`, the slug being derived from the act's title.

## Sources

- e-Sbírka open data (metadata dumps, published by the Ministry of the Interior; see the
  National Open Data Catalogue https://data.gov.cz for terms of use):
  https://opendata.eselpoint.gov.cz/datove-sady-esbirka/ — `006PravniAktMetadata.json.gz` is used
  to list acts and their validity.
- e-Sbírka public REST API used by the e-sbirka.gov.cz web application (texts as XHTML fragments):
  `https://e-sbirka.gov.cz/sbr-cache/dokumenty-sbirky/{/sb/<year>/<number>}` and
  `…/fragmenty?cisloStranky=<n>`.

## Licence / copyright

Legal regulations are excluded from copyright protection under § 3(a) of the Czech Copyright Act
(zákon č. 121/2000 Sb., autorský zákon: *úřední dílo* — "právní předpis"), so the texts are in
the public domain. Only the texts as promulgated / authenticated in e-Sbírka have legal force;
check e-Sbírka for the legal status of a given consolidated version.
This repository is not an official publication.

## Regenerating

```sh
pip install -r scripts/requirements.txt
python scripts/fetch.py --raw ../_raw/cz          # metadata dump + API, cached under _raw/cz/api
python scripts/convert.py --raw ../_raw/cz --clean # writes the Markdown tree into the repo
```

`fetch.py` uses 3 concurrent connections with a `LawCodex/1.0` User-Agent and retries with
backoff; a full run makes about 10,000 API requests (~2 hours). Cached files are reused on
subsequent runs; delete `_raw/cz/api` to refresh all texts.
