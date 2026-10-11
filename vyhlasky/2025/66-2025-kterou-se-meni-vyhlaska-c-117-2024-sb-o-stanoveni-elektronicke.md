---
title: "Vyhláška č. 66/2025 Sb., kterou se mění vyhláška č. 117/2024 Sb., o stanovení elektronické komunikace pro plnění informačních povinností zaměstnavatele při zaměstnávání zaměstnanců ze zahraničí"
identifier: "66/2025 Sb."
eli: "https://e-sbirka.gov.cz/eli/cz/sb/2025/66/2025-04-01"
type: decree
jurisdiction: cz
language: cs
date: 2025-03-06
effective: 2025-04-01
last_amended: 2025-04-01
status: in_force
source: "https://e-sbirka.gov.cz/sb/2025/66"
retrieved: 2026-10-11
---

# Vyhláška č. 66/2025 Sb., kterou se mění vyhláška č. 117/2024 Sb., o stanovení elektronické komunikace pro plnění informačních povinností zaměstnavatele při zaměstnávání zaměstnanců ze zahraničí

66

VYHLÁŠKA

ze dne 6. března 2025,

kterou se mění vyhláška č. 117/2024 Sb., o stanovení elektronické komunikace pro plnění informačních povinností zaměstnavatele při zaměstnávání zaměstnanců ze zahraničí

Ministerstvo práce a sociálních věcí stanoví podle § 87 odst. 4 zákona č. 435/2004 Sb., o zaměstnanosti, ve znění zákona č. 408/2023 Sb.:

## Čl. I

Vyhláška č. 117/2024 Sb., o stanovení elektronické komunikace pro plnění informačních povinností zaměstnavatele při zaměstnávání zaměstnanců ze zahraničí, se mění takto:

1\. V příloze nadpis úvodní neoznačené části zní:

> „A) Specifikace komunikace“.

2\. V příloze část C zní:

> „C) Obsah a datová struktura

> Všechny atributy jsou povinné, pokud není v popisu uvedeno jinak. Datová struktura je opisem přesné definice XSD https://www.mpsv.cz/documents/20142/6902273/okp-ciz-ws_v2.xsd. Technická dokumentace je zveřejněna na internetových stránkách http://developers.mpsv.cz/.

> Datová věta podání Informační karty prostřednictvím elementu CizInformace

> <table><tbody><tr><th>Element</th><th>Atribut</th><th colspan="3">Typ</th><th>Popis</th></tr><tr><td rowspan="22">CizInformace</td><td>idPozadavku</td><td colspan="3">idPozadavku</td><td>Formát podle XSD zveřejněného na stránkách: http://www.mpsv.cz/ <br> developers.mpsv.cz</td></tr><tr><td>identifikatorPredchozihoOznameni</td><td colspan="3">identifikatorPredchozihoOznameni</td><td><b>Nepovinné</b></td></tr><tr><td>krpKod</td><td colspan="3">KrajskaPobockaUp</td><td>Výběr podle příslušné krajské pobočky Úřadu práce podle místa výkonu práce</td></tr><tr><td>cizinecInformace</td><td colspan="3">CizinecInformace</td><td></td></tr><tr><td>udajeInformace</td><td colspan="3">UdajeInformace</td><td></td></tr><tr><td>vykonPrace</td><td colspan="3">VykonPrace</td><td></td></tr><tr><td rowspan="16">smlouvaCr<br> smlouvaZahr</td><td colspan="3" rowspan="16">Výběr z:<br> • smlouvaCr<br> • smlouvaZahr</td><td rowspan="16">"smlouvaCr" vyplňuje zaměstnavatel se sídlem v ČR, který uzavřel pracovní smlouvu, dohodu o pracovní činnosti nebo dohodu o provedení práce s občanem EU/EHP nebo Švýcarska, jeho rodinným příslušníkem, nebo cizincem, který nepotřebuje pracovní oprávnění podle § 98 zákona o zaměstnanosti.<br><br> Jedná se o případy variantaPracovnihoVztahuKod=ZAMESTNAVATEL_V_CR nebo variantaPracovnihoVztahuKod=AGENTURA_UZIVATEL.<br><br> "smlouvaZahr" vyplňuje<br> zaměstnavatel se sídlem mimo ČR v případě, že občan EU/EHP nebo Švýcarska, nebo jeho rodinný příslušník, případně cizinec, který nepotřebuje pracovní oprávnění podle § 98 zákona o zaměstnanosti, byl vnitropodnikově převeden k výkonu práce do odštěpného závodu nebo obchodní korporace na území ČR, nebo vyslán svým zahraničním zaměstnavatelem na základě smlouvy s českou fyzickou nebo právnickou osobou k výkonu práce na území ČR k plnění úkolů vyplývajících z této smlouvy - a jehož vyslání nespadá do působnosti směrnice 96/71/ES o vysílání pracovníků v rámci poskytování služeb. Odštěpný závod nebo obchodní korporace, nebo česká fyzická nebo právnická osoba, se uvádí do elementu "odstepZavodObchKorporace". Jedná se případ variantaPracovnihoVztahuKod=VNITROPODNIKOVE_PREVEDENI.</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr><td rowspan="2">smlouvaCr</td><td>zamestnavatelVCr</td><td colspan="3">SubjektVCr</td><td></td></tr><tr><td></td><td colspan="3"></td><td></td></tr><tr><td rowspan="2">smlouvaZahr</td><td>zamestnavatelZahr</td><td colspan="3">SubjektZahr</td><td></td></tr><tr><td>odstepZavodObchKorporace</td><td colspan="3">SubjektVCr</td><td></td></tr></tbody></table>

> **Datová věta Sdělení – nástup**

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="7">CizSdeleniNastup</td><td>idPozadavku</td><td>idPozadavku</td><td>Formát podle XSD</td></tr><tr><td>identifikatorPredchozihoOznameni</td><td>identifikatorPredchozihoOznameni</td><td><b>Nepovinné</b></td></tr><tr><td>krpKod</td><td>KrajskaPobockaUp</td><td>Výběr podle příslušné krajské pobočky Úřadu práce podle místa výkonu práce</td></tr><tr><td>cizinecSdeleniNastup</td><td>CizinecSdeleniNastup</td><td></td></tr><tr><td>udajeSdeleniNastup</td><td>UdajeSdeleniNastup</td><td></td></tr><tr><td>vykonPrace</td><td>VykonPrace</td><td></td></tr><tr><td>zamestnavatelVCr</td><td>SubjektVCr</td><td></td></tr></tbody></table>

> **Datová věta Sdělení – ukončení**

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="7">CizSdeleniUkonceni</td><td>idPozadavku</td><td>idPozadavku</td><td>Formát podle XSD</td></tr><tr><td>identifikatorPredchozihoOznameni</td><td>identifikatorPredchozihoOznameni</td><td><b>Nepovinné</b></td></tr><tr><td>krpKod</td><td>KrajskaPobockaUp</td><td>Výběr podle příslušné krajské pobočky Úřadu práce podle místa výkonu práce</td></tr><tr><td>cizinecSdeleniUkonceni</td><td>CizinecSdeleniUkonceni</td><td></td></tr><tr><td>udajeSdeleniUkonceni</td><td>UdajeSdeleniUkonceni</td><td></td></tr><tr><td>vykonPrace</td><td>VykonPrace</td><td></td></tr><tr><td>zamestnavatelVCr</td><td>SubjektVCr</td><td></td></tr></tbody></table>

> **Datové typy**

> Formáty a omezení jednotlivých atributů jsou uvedeny v XSD.

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="3">AdresaVCr</td><td>adresaKod polozky</td><td></td><td>Výběr – RUIAN kód nebo manuální zadání (polozky)</td></tr><tr><td>adresaKod</td><td>decimal</td><td>Kód adresy z RUIAN – vyplněno pouze pro standardní adresy</td></tr><tr><td>polozky</td><td></td><td></td></tr><tr><td rowspan="9">polozky</td><td>obec</td><td>string</td><td>Název obce</td></tr><tr><td>castObce</td><td>string</td><td><b>Nepovinné</b><br> Název části obce</td></tr><tr><td>ulice</td><td>string</td><td><b>Nepovinné</b><br> Název ulice</td></tr><tr><td>cisPopis<br> cisEvid</td><td></td><td><b>Výběr, Nepovinné</b></td></tr><tr><td>cisPopis</td><td>int</td><td>Číslo popisné</td></tr><tr><td>cisEvid</td><td>int</td><td>Číslo evidenční</td></tr><tr><td>cisOrient</td><td>int</td><td><b>Nepovinné</b><br> Číslo orientační</td></tr><tr><td>cisOrientPism</td><td>string</td><td><b>Nepovinné</b><br> Koncové písmeno čísla orientačního – jen při zadaném čísle orientačním</td></tr><tr><td>psc</td><td>decimal</td><td>PSČ</td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="4">AdresaZahr</td><td>radek1</td><td>string</td><td>První řádek zahraniční adresy – zpravidla ulice a číslo popisné nebo evidenční</td></tr><tr><td>radek2</td><td>string</td><td><b>Nepovinné</b><br> Druhý řádek zahraniční adresy – zpravidla ZIP kód a město</td></tr><tr><td>radek3</td><td>string</td><td><b>Nepovinné</b><br> Třetí řádek zahraniční adresy – Zpravidla okres, region, země</td></tr><tr><td>statKod</td><td>StatKod</td><td>Číselník StatKod</td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="8">CizinecMin</td><td>prijmeni</td><td>string</td><td>Příjmení cizince</td></tr><tr><td>jmeno</td><td>string</td><td>Jméno cizince</td></tr><tr><td>datumNarozeni</td><td>date</td><td>Datum narození cizince</td></tr><tr><td>pohlaviKod</td><td><b>TypPohlavi</b></td><td><b>Číselník</b><b>TypPohlavi</b></td></tr><tr><td>mistoNarozeni</td><td>string</td><td>Místo narození cizince – město, stát</td></tr><tr><td>statniObcanstviKod</td><td>StatKod</td><td>Výběr ze seznamu zemí.<br><br> Nemůže být vybrán žádný stát EU, EHP a Švýcarsko.</td></tr><tr><td>rodneCislo</td><td>RodneCislo</td><td><b>Nepovinné</b><br> Rodné číslo přidělené v ČR.</td></tr><tr><td>evidCisloPojistence</td><td>string</td><td><b>Nepovinné</b><br> EČP - evidenční číslo pojištěnce</td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="6">CizinecInformace</td><td></td><td></td><td>Rozšiřuje Element<br> CizinecMin</td></tr><tr><td>vzdelaniKod</td><td>DosazeneVzdelani</td><td><b>Číselník<br> DosazeneVzdelani</b>.<br> Nejvyšší dosažený stupeň vzdělání cizince</td></tr><tr><td>dokladZahr</td><td>IdentifkacniDoklad</td><td>Zahraniční identifikační doklad cizince. Byl-li cizinci vydán platný doklad v ČR, je možné uvést číslo tohoto dokladu a vydávající orgán v ČR.</td></tr><tr><td>adresaTrvalyPobytZahr</td><td>AdresaZahr</td><td>Adresa, kde má hlášená osoba (cizinec) trvalý pobyt. Zahraniční adresa, vylučuje vyplnění adresy trvalého pobytu v ČR.</td></tr><tr><td>adresaTrvalyPobytVCr</td><td>AdresaVCr</td><td>Adresa, kde má hlášená osoba (cizinec) trvalý pobyt. Adresa v ČR, vylučuje vyplnění adresy trvalého pobytu v zahraničí.</td></tr><tr><td>adresaProDorucovani</td><td>AdresaVCr</td><td></td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="5">CizinecSdeleniNastup</td><td></td><td></td><td>Rozšiřuje Element<br> CizinecMin</td></tr><tr><td>vzdelaniKod</td><td>DosazeneVzdelani</td><td><b>Číselník<br> DosazeneVzdelani</b>.<br> Nejvyšší dosažený<br> stupeň vzdělání cizince</td></tr><tr><td>dokladZahr</td><td>IdentifkacniDoklad</td><td>Zahraniční identifikační doklad cizince. Byl-li cizinci vydán platný doklad v ČR, je možné uvést číslo tohoto dokladu a vydávající orgán v ČR.</td></tr><tr><td>adresaTrvalyPobytZahr</td><td>AdresaZahr</td><td>Adresa, kde má hlášená osoba (cizinec) trvalý pobyt. Zahraniční adresa.</td></tr><tr><td>adresaProDorucovani</td><td>AdresaVCr</td><td></td></tr></tbody></table>

> | Element | Atribut | Typ | Popis |
> |---|---|---|---|
> | CizinecSdeleniUkonceni | | | Rozšiřuje Element<br> CizinecMin |

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="6">SubjektVCr</td><td>nazev</td><td>string</td><td>Název subjektu, 1-250 znaků</td></tr><tr><td>ico<br> rodneCislo</td><td></td><td>Výběr, IČO, pokud je přiděleno, jinak rodné číslo</td></tr><tr><td>ico</td><td>string</td><td>IČO, 8 znaků [0-9]</td></tr><tr><td>rodneCislo</td><td>RodneCislo</td><td>Rodné číslo fyzické osoby, která nepodniká</td></tr><tr><td>adresaSidla</td><td>AdresaVCr</td><td></td></tr><tr><td>kontakt</td><td>Kontakt</td><td><b>Nepovinné</b></td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="3">Kontakt</td><td>jmeno</td><td>string</td><td><b>Nepovinné</b><br> Jméno, 1-100 znaků</td></tr><tr><td>telefon</td><td>string</td><td><b>Nepovinné</b><br> Telefon, 1-50 znaků</td></tr><tr><td>email</td><td>string</td><td><b>Nepovinné</b><br> E-mail, 1-250 znaků</td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="4">UdajeInformace</td><td>statutCizinceKod</td><td>StatutCizince</td><td><b>Číselník StatutCizince.</b><br> Statut vstupu cizince na trh práce podle zákona o zaměstnanosti</td></tr><tr><td>variantaPracovnihoVztahuKod</td><td>VariantaPracovnihoVztahu</td><td><b>Číselník</b><br><b>VariantaPracovnihoVztahu.</b><br> Varianta pracovního vztahu</td></tr><tr><td>pracpravniVztahKod</td><td>PracpravniVztah</td><td><b>Číselník PracpravniVztah. Nepovinné v případě<br> variantaPracovnihoVztahuKod= VNITROPODNIKOVE_PREVEDENI.</b><br> Druh pracovněprávního vztahu</td></tr><tr><td>vzdelaniKod</td><td>DosazeneVzdelani</td><td><b>Číselník DosazeneVzdelani.</b><br> Požadovaný stupeň vzdělání pro výkon práce</td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="8">UdajeSdeleniSpolecne</td><td>druhPovoleniKod</td><td>DruhPovoleni</td><td><b>Číselník DruhPovoleni.</b><br> Druh povolení (pracovního oprávnění)</td></tr><tr><td>cisloPovoleni</td><td>string</td><td>Číslo jednací povolení k zaměstnání nebo číslo zaměstnanecké karty, modré karty nebo karty vnitropodnikově převedeného zaměstnance.</td></tr><tr><td>vydanoDne</td><td>date</td><td>Datum vydání povolení k zaměstnání, zaměstnanecké karty, modré karty nebo karty vnitropodnikově převedeného zaměstnance</td></tr><tr><td>platnostDo</td><td>date</td><td>Datum platnosti povolení k zaměstnání, zaměstnanecké karty, modré karty nebo karty vnitropodnikově převedeného zaměstnance</td></tr><tr><td>vydalaKrpKod</td><td>KrajskaPobockaUp</td><td><b>Nepovinné</b><br> Zkratka určující krajskou pobočku Úřadu práce, která vydala povolení k zaměstnání.</td></tr><tr><td>cisloVolnPracMista</td><td>string</td><td><b>Nepovinné</b><br> Číslo volného pracovního místa v případě povolení k zaměstnání, zaměstnanecké karty či modré karty. Formát dle XSD.</td></tr><tr><td>formaZamestnaniKod</td><td>FormaZamestnani</td><td><b>Číselník FormaZamestnani</b><br> Forma zaměstnání cizince na území ČR.</td></tr><tr><td>agenturaPrace</td><td>boolean</td><td><b>Nepovinné</b><br> Jedná se o zaměstnání za účelem dočasného přidělení agenturou práce k výkonu práce u uživatele</td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="2">UdajeSdeleniNastup</td><td></td><td>Rozšiřuje element UdajeSdeleniSpolecne</td><td>Společné údaje pro případy nástupu, nenastoupení a ukončení zaměstnání nebo výkonu práce na území ČR cizince, kterému bylo vydáno povolení k zaměstnání, zaměstnanecká karta, karta vnitropodnikově převedeného zaměstnance nebo modrá karta, nebo při změně dříve nahlášených údajů.</td></tr><tr><td>vzdelaniKod</td><td>DosazeneVzdelani</td><td><b>Číselník DosazeneVzdelani.</b><br> Požadovaný stupeň vzdělání pro výkon práce</td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="4">UdajeSdeleniUkonceni</td><td></td><td>Rozšiřuje element UdajeSdeleniSpolecne</td><td>Společné údaje pro případy nástupu, nenastoupení a ukončení zaměstnání nebo výkonu práce na území ČR cizince, kterému bylo vydáno povolení k zaměstnání, zaměstnanecká karta, karta vnitropodnikově převedeného zaměstnance nebo modrá karta, nebo při změně dříve nahlášených údajů.</td></tr><tr><td>typSdeleniKod</td><td>TypSdeleni</td><td>Sdělení zaměstnavatele – například nenastoupení nebo ukončení zaměstnání</td></tr><tr><td>datumUkonceni</td><td>Date</td><td>Nepovinné, pokud typSdeleniKod je NEPOTREBUJE_POVOLENI, jinak povinné. Datum ukončení nebo předčasného ukončení zaměstnání</td></tr><tr><td>povolNepotrebujeOd</td><td>Date</td><td>Povinné, pokud typSdeleniKod je NEPOTREBUJE_POVOLENI, jinak nepovinné. Datum, od kdy nepotřebuje povolení k zaměstnání, zaměstnaneckou kartu, kartu vnitropodnikového převedení nebo modrou kartu</td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="9">VykonPrace</td><td>identifikatorPracovnihoVztahu</td><td>string</td><td>Nepovinné<br> Identifikátor daného pracovněprávního vztahu cizince u zaměstnavatele, např. číslo pracovní smlouvy, pokud zaměstnavatel pracovněprávní vztah pro svou evidenci blíže označuje</td></tr><tr><td>vykonPraceOd</td><td>date</td><td>Výkon práce od</td></tr><tr><td>vykonPraceDo</td><td>date</td><td><b>Nepovinné</b><br> Datum plánovaného ukončení zaměstnání. Vyplňte v případě, že jste při nástupu zadali datum ukončení zaměstnání, a vyplňte právě tímto dříve zadaným datem.</td></tr><tr><td>czIscoKod</td><td>CZ-ISCO</td><td>Klasifikace zaměstnání – číselník CZ-ISCO</td></tr><tr><td>czNaceKod</td><td>CZ-NACE</td><td>Klasifikace ekonomických činností – číselník CZ-NACE</td></tr><tr><td>vzdelaniKod</td><td>DosazeneVzdelani</td><td><b>Číselník<br> DosazeneVzdelani.</b><br> Požadovaný stupeň vzdělání pro výkon práce</td></tr><tr><td>adresaMistaVykonu textMistaVykonu</td><td></td><td>Výběr, viz popis atributů výběru</td></tr><tr><td>adresaMistaVykonu</td><td>AdresaVCr</td><td>Adresa místa výkonu práce pro případ, kdy je místo výkonu konkrétní adresa</td></tr><tr><td>textMistaVykonu</td><td>string</td><td>Textová varianta určení místa výkonu práce pro případ, kdy není místo výkonu konkrétní adresa</td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr></tr><tr><td rowspan="3">SubjektZahr</td><td>nazev</td><td>string</td><td>Název zahraničního subjektu 1-250 znaků</td></tr><tr><td>adresaSidla</td><td>AdresaZahr</td><td></td></tr><tr><td>kontakt</td><td>Kontakt</td><td>Kontaktní informace zahraničního subjektu</td></tr></tbody></table>

> <table><tbody><tr><th>Element</th><th>Atribut</th><th>Typ</th><th>Popis</th></tr><tr><td rowspan="2">IdentifkacniDoklad</td><td>cisloDokladu</td><td>string</td><td>Číslo identifikačního dokladu 1-20 znaků</td></tr><tr><td>nazevOrganu</td><td>string</td><td>Název vydávajícího orgánu identifikačního dokladu 1-250 znaků</td></tr></tbody></table>

> | Element | Atribut | Typ | Popis |
> |---|---|---|---|
> | date | | string | Textový řetězec data ve formátu RFC 3339, section 5.6, YYYY-MM-DD |

> | Element | Atribut | Typ | Popis |
> |---|---|---|---|
> | RodneCislo | | string | Textový řetězec, 9-10 znaků, povolené znaky [09] (udává se vždy bez lomítka) |

> | Element | Atribut | Typ | Popis |
> |---|---|---|---|
> | idPozadavku | | string | ([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})│(\\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\\}) |

> | Element | Atribut | Typ | Popis |
> |---|---|---|---|
> | identifikatorPredchozihoOznameni | | string | Nejvíce 50 znaků. V případě oznámení změny nebo ukončení výkonu práce slouží k identifikaci předchozího oznámení, ke kterému změna nebo ukončení přísluší. Pokud ji zaměstnavatel nezná, nemusí ji vyplňovat. V komplikovaných případech (např. oprava původně chybně zadaného jména a příjmení i data narození cizince) může dojít k duplicitám v evidenci. Jako hodnotu elementu "identifikatorPredchozihoOznameni" je možné uvést "identifikátor oznámení", který byl zaměstnavateli přidělen při libovolném předchozím či prvním oznámení, nebo "idPozadavku", které zaměstnavatel uvedl při libovolném předchozím či prvním oznámení, nebo číslo jednací daného výkonu práce z evidence Úřadu práce, je-li zaměstnavateli známo. |

> **Číselníky**

> **Číselníky jsou popsány pomocí této šablony tabulky**

> | **Název číselníku** | Stručný popis číselníku |
> |---|---|
> | Kód číselníku | Popis kódu číselníku. |
> | Kód číselníku | Popis kódu číselníku. |

> | **VariantaPracovnihoVztahu** | Varianta pracovního vztahu |
> |---|---|
> | ZAMESTNAVATEL_V_CR | Zaměstnavatel se sídlem v ČR, který uzavřel smlouvu s cizincem |
> | AGENTURA_UZIVATEL | Zaměstnavatel se sídlem v ČR, který dočasně přidělil cizince k výkonu práce u fyzické nebo právnické osoby se sídlem v ČR |
> | VNITROPODNIKOVE_PREVEDENI | Zaměstnavatel se sídlem mimo ČR, který vyslal nebo vnitropodnikově převedl cizince k výkonu práce do odštěpného závodu nebo obchodní korporace na území ČR a nespadá pod směrnici o vyslání 96/71/ES |

> | **PracpravniVztah** | Druh pracovněprávního vztahu |
> |---|---|
> | PRACOVNI_POMER | Pracovní poměr |
> | DOHODA_O_PRACOVNI_CINNOSTI | Dohoda o pracovní činnosti |
> | DOHODA_O_PROVEDENI_PRACE | Dohoda o provedení práce |

> | **StatutCizince** | Statut vstupu cizince na trh práce podle zákona o zaměstnanosti |
> |---|---|
> | OBCAN_EU | Občan EU |
> | OBCAN_EHP | Občan EHP (Norsko, Island a Lichtenštejnsko) |
> | OBCAN_SVYCARSKA | Občan Švýcarska |
> | OBCAN_SPOJENEHO_KRALOVSTVI_VELKE_BRITANIE_A_SEVERNIHO_IRSKA | Občan Spojeného království Velké Británie a Severního Irska |
> | RODINNY_PRISLUSNIK_OBCANA_EU_EHP_NEBO_SVYCARSKA | Rodinný příslušník občana EU/EHP nebo Švýcarska (včetně ČR) |
> | POVOLEN_TRVALY_POBYT_DOCASNA_OCHRANA | § 98 písm. a): Povolen trvalý pobyt – dočasná ochrana Ukrajina |
> | POVOLEN_TRVALY_POBYT_MIMO_DOCASNOU_OCHRANU | § 98 písm. a): Povolen trvalý pobyt |
> | RODINNY_PRISLUS_CLENA_DIPLOMAT_MISE | § 98 písm. b): Rodinný příslušník člena diplomatické mise |
> | UDELEN_AZYL_NEBO_DOPLNKOVA_OCHRANA | § 98 písm. c): Udělen azyl nebo doplňková ochrana |
> | KRATKODOBA_PRAC_CINNOST_DO_7_DNU | § 98 písm. d): Krátkodobá pracovní činnost (do 7 dnů) |
> | MEZINARODNI_SMLOUVA | § 98 písm. e): Mezinárodní smlouva |
> | PRIPRAVA_NA_BUDOUCI_POVOLANI | § 98 písm. j): Soustavná příprava na budoucí povolání |
> | DLOUHODOBY_POBYT_SPOLEC_SOUZITI_RODINY | § 98 písm. l): Dlouhodobý pobyt za účelem společného soužití rodiny |
> | REZIDENT_JINEHO_STATU_EU | § 98 písm. m): Rezident jiného členského státu EU |
> | SOUSTAVNA_VZDEL_NEBO_VED_CINNOST | § 98 písm. n): Soustavná vzdělávací nebo vědecká činnost |
> | ZISKANE_VYS_ODBOR_NEBO_VS_VZDELANI | § 98 písm. o): Získané SŠ, VOŠ nebo VŠ vzdělání |
> | DLOUHODOBY_POBYT_ZA_UCELEM_OCHRANY | § 98 písm. p): Dlouhodobý pobyt za účelem ochrany |
> | DUCHOVNI_CIRKVE_REGISTROVANE_V_CR | § 98 písm. r): Duchovní církve nebo náboženské společnosti v ČR |
> | VNITROPODNIKOVE_PREVEDENY_ZAMESTNANEC_Z_EU | § 98 písm. s): Vnitropodnikově převedený zaměstnanec (v rámci EU) |
> | VYKON_PRACE_V_ZAJMU_CR | § 98 písm. t): Výkon práce v zájmu ČR |
> | OBCAN_STATU_NEVYZADUJICI_PRACOVNI_OPRAVNENI_WHITELIST | § 98 písm. u): Občan státu nevyžadujícího pracovní oprávnění (whitelist) |
> | UMELECKA_CINNOST | § 98 písm. v): Umělecká činnost |
> | VYSLANI_ZVYSOVANI_DOVEDNOSTI | § 98a: Vyslání – zvyšování dovedností |

> | **DosazeneVzdelani** | Kategorie dosaženého stupně vzdělání podle Klasifikace kmenových oborů vzdělání (KKOV) |
> |---|---|
> | A | Bez vzdělání |
> | B | Neúplné základní vzdělání |
> | C | Základní vzdělání |
> | D | Nižší střední vzdělání |
> | E | Nižší střední odborné vzdělání |
> | H | Střední odborné vzdělání s výučním listem |
> | J | Střední nebo střední odborné vzdělání bez maturity i výučního listu |
> | K | Úplné střední všeobecné vzdělání |
> | L | Úplné střední odborné vzdělání s vyučením i maturitou |
> | M | Úplné střední odborné vzdělání s maturitou (bez vyučení) |
> | N | Vyšší odborné vzdělání |
> | P | Vyšší odborné vzdělání v konzervatoři |
> | R | Vysokoškolské bakalářské vzdělání |
> | T | Vysokoškolské magisterské vzdělání |
> | V | Vysokoškolské doktorské vzdělání |

> | **TypPohlavi** | Číselník pohlaví je definován číselníky ISZR |
> |---|---|
> | M | Muž |
> | F | Žena |

> | **DruhPovoleni** | Druh povolení (pracovního oprávnění) |
> |---|---|
> | POVOLENI_K_ZAMESTNANI | Povolení k zaměstnání |
> | ZAMESTNANECKA_KARTA | Zaměstnanecká karta |
> | MODRA_KARTA | Modrá karta |
> | VNITROPODNIKOVE_PREVEDENI | Karta vnitropodnikově převedeného zaměstnance |

> | **TypSdeleni** | Typ sdělení |
> |---|---|
> | UKONCENI_ZAMESTNANI | Ukončení zaměstnání |
> | NENASTOUPENI | Nenastoupení cizince do zaměstnání |
> | PREDCASNE_UKONCENI_VYPOVED_DOHODA_52AE | Předčasné ukončení zaměstnání – výpověď nebo dohoda z důvodů uvedených v § 52 písm. a) – e) zákoníku práce |
> | PREDCASNE_UKONCENI_OKAMZITE_ZRUSENI_56 | Předčasné ukončení zaměstnání – okamžité zrušení dle § 56 zákoníku práce |
> | PREDCASNE_UKONCENI_JINY_DUVOD | Předčasné ukončení zaměstnání – z jiných důvodů |
> | NEPOTREBUJE_POVOLENI | Cizinec již nepotřebuje povolení k zaměstnání / zaměstnaneckou kartu / modrou kartu / kartu vnitropodnikově převedeného zaměstnance |

> | **FormaZamestnani** | Forma zaměstnání cizince na území ČR |
> |---|---|
> | PRACOVNI_POMER | Pracovněprávní vztah k zaměstnavateli se sídlem v ČR– pracovní poměr |
> | DOHODA_O_PRAC_CINNOSTI | Pracovněprávní vztah k zaměstnavateli se sídlem v ČR – dohoda o pracovní činnosti |
> | VYSLANI_CR | Vyslání zahraničním zaměstnavatelem k plnění úkolů na území ČR u české fyzické nebo právnické osoby |
> | VNITROPODNIKOVE_PREVEDENI | Vnitropodnikové převedení zaměstnance |

> | **KrajskaPobockaUp** | Krajská pobočka Úřadu práce |
> |---|---|
> | MHMP | Krajská pobočka pro hlavní město Prahu |
> | JMK | Krajská pobočka v Brně |
> | JCK | Krajská pobočka v Českých Budějovicích |
> | HKK | Krajská pobočka v Hradci Králové |
> | VYK | Krajská pobočka v Jihlavě |
> | KVK | Krajská pobočka v Karlových Varech |
> | LBK | Krajská pobočka v Liberci |
> | OLK | Krajská pobočka v Olomouci |
> | MSK | Krajská pobočka v Ostravě |
> | PAK | Krajská pobočka v Pardubicích |
> | PMK | Krajská pobočka v Plzni |
> | SCK | Krajská pobočka v Příbrami |
> | ULK | Krajská pobočka v Ústí nad Labem |
> | ZLK | Krajská pobočka ve Zlíně |

> | **StatKod** | Číselník Českého statistického úřadu https://www.czso.cz/csu/czso/ciselnik_zemi\_-czem-. Používá se výhradně trojmístný alfabetický kód. Rozšířený číselník pokrývající logiku výběru zemí v jednotlivých atributech je zveřejněn na https://developers.mpsv.cz/ |
> |---|---|

> | **CZ-NACE** | Klasifikace ekonomických činností – číselník CZ-NACE https://csu.gov.cz/klasifikace_ekonomickych_cinnosti_cz_nace Používá se vždy minimálně dvoupísmenný kód, tedy například místo kódu *1* kód *01*. Při výběru podkategorií se nepoužívají tečky, tedy například podkategorie *1.11* se zapíše jako *0111*. |
> |---|---|

> | **CZ-ISCO** | Klasifikace zaměstnání – číselník CZ-ISCO https://www.czso.cz/csu/czso/klasifikace_zamestnani\_-cz_isco-<br> Používá se vždy minimálně dvoupísmenný kód, tedy například místo kódu *1* kód *01*. Při výběru podkategorií se nepoužívají tečky, tedy například podkategorie *1.11* se zapíše jako *0111*. |
> |---|---|
>
> “.

## Čl. II – Přechodné ustanovení

Do 30. června 2025 lze postupovat podle vyhlášky č. 117/2024 Sb., ve znění účinném přede dnem nabytí účinnosti této vyhlášky.

## Čl. III – Účinnost

Tato vyhláška nabývá účinnosti dnem 1. dubna 2025.

Ministr práce a sociálních věcí:

Ing. Jurečka v. r.
