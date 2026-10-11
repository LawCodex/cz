---
title: "Vyhláška č. 368/2025 Sb., o provedení některých ustanovení zákona o pomoci v hmotné nouzi"
identifier: "368/2025 Sb."
eli: "https://e-sbirka.gov.cz/eli/cz/sb/2025/368/2026-05-01"
type: decree
jurisdiction: cz
language: cs
date: 2025-09-22
effective: 2025-10-01
last_amended: 2026-05-01
status: in_force
source: "https://e-sbirka.gov.cz/sb/2025/368"
retrieved: 2026-10-11
---

# Vyhláška č. 368/2025 Sb., o provedení některých ustanovení zákona o pomoci v hmotné nouzi

368

VYHLÁŠKA

ze dne 22. září 2025

o provedení některých ustanovení zákona o pomoci v hmotné nouzi

Ministerstvo práce a sociálních věcí stanoví podle § 80 zákona č. 111/2006 Sb., o pomoci v hmotné nouzi, ve znění zákona č. 382/2008 Sb., zákona č. 366/2011 Sb. a zákona č. 152/2025 Sb., (dále jen ,,zákon“) k provedení § 29, § 50a odst. 2, § 50b odst. 1 a § 63 odst. 3 zákona:

## § 2 – Specifikace komunikace mezi orgány pomoci v hmotné nouzi a peněžním ústavem a formát, obsah a struktura datové zprávy

(K § 50a odst. 2 zákona)

Specifikace komunikace mezi orgánem pomoci v hmotné nouzi a bankou, pobočkou zahraniční banky, spořitelním a úvěrním družstvem, institucí elektronických peněz, pobočkou zahraniční instituce elektronických peněz, vydavatelem elektronických peněz malého rozsahu, platební institucí, pobočkou zahraniční platební instituce nebo poskytovatelem platebních služeb malého rozsahu (dále jen „peněžní ústav“) a formát, obsah a struktura datové zprávy jsou stanoveny v příloze č. 1 k této vyhlášce. Veškeré vyměňované XML soubory jsou zapečetěny kvalifikovanou elektronickou pečetí (dále jen „pečeť“).

## § 3 – Specifikace komunikace mezi orgánem pomoci v hmotné nouzi a zaměstnavatelem a formát, obsah a struktura datové zprávy

(K § 50b odst. 1 zákona)

Specifikace komunikace mezi orgánem pomoci v hmotné nouzi a zaměstnavatelem a formát, obsah a struktura datové zprávy jsou stanoveny v příloze č. 2 k této vyhlášce.

## § 4 – Specifikace komunikace mezi orgánem pomoci v hmotné nouzi a dodavatelem plynu nebo elektřiny a formát, obsah a struktura datové zprávy

(K § 50b odst. 1 zákona)

Specifikace komunikace mezi orgánem pomoci v hmotné nouzi a dodavatelem plynu nebo elektřiny a formát, obsah a struktura datové zprávy jsou stanoveny v příloze č. 3 k této vyhlášce.

## § 5 – Náležitosti průkazu zaměstnance oprávněného k vykonávání činností sociální práce

(K § 63 odst. 3 zákona)

​Průkaz zaměstnance obce zařazeného do pověřeného obecního úřadu nebo obecního úřadu obce s rozšířenou působností jako sociálního pracovníka a zaměstnance státu zařazeného k výkonu práce v újezdním úřadu jako sociálního pracovníka, kterým se prokazuje při vstupu do obydlí za účelem vykonávání činností sociální práce, obsahuje tyto náležitosti:

a) jméno, popřípadě jména, příjmení a titul zaměstnance,

b) fotografii zaměstnance,

c) označení „sociální pracovník“,

d) označení příslušného úřadu, který průkaz vydal, otisk úředního razítka a podpis vedoucího zaměstnance,

e) dobu platnosti průkazu.

## § 6 – Účinnost

(1) Tato vyhláška nabývá účinnosti dnem 1. října 2025.

(2) Ustanovení § 1 pozbývá platnosti uplynutím dne 30. dubna 2026.

Ministr:

Ing. Jurečka v. r.

### Příloha č. 1 ​

#### Specifikace komunikace mezi orgány pomoci v hmotné nouzi a peněžním ústavem a formát, obsah a struktura datové zprávy

**​**

**A) Specifikace komunikace mezi peněžním ústavem a orgánem pomoci v hmotné nouzi**

1\) Orgán pomoci v hmotné nouzi odešle písemnou žádost jako zprávu obsahující dokument výzvy a XML soubor z datové schránky orgánu pomoci v hmotné nouzi do datové schránky peněžního ústavu. Orgán pomoci v hmotné nouzi do předmětu datové zprávy vloží pouze text “XMLOPHNSOUC”.

2\) Peněžní ústav na písemnou žádost orgánu pomoci v hmotné nouzi odešle zprávu s XML souborem s požadovanými daty do datové schránky orgánu pomoci v hmotné nouzi z datové schránky peněžního ústavu. Pro vytvoření XML souboru odpovědi peněžní ústav využije vlastní technické prostředky. Peněžní ústav do předmětu datové zprávy vloží pouze text “XMLOPHNSOUC”.

**B) Formát a struktura datové zprávy**

Datová zpráva pro komunikaci mezi orgánem pomoci v hmotné nouzi a peněžním ústavem je výhradně ve formátu XML. XML soubor je kódován v UTF-8. Jméno souboru je tvořeno kódem orgánu pomoci v hmotné nouzi, kódem peněžního ústavu a unikátním identifikátorem vytvořeným orgánem pomoci v hmotné nouzi při vytváření dotazu, a to podle následujících pravidel:

| <br>**Pořadí** | <br>**Část** | <br>**Délka** | <br>**Popis** |
|---|---|---|---|
| <br>1 | <br>*KodOPHN* | <br>3 | <br>Kód dotazujícího se orgánu pomoci v hmotné nouzi. |
| <br>2 | <br>„-„ | <br>1 | <br>Oddělovač. |
| <br>3 | <br>*KodBanky* | <br>4 | <br>Kód dotazovaného peněžního ústavu. |
| <br>4 | <br>- | <br>1 | <br>Oddělovač. |
| <br>5 | <br>*CisloDavky* | <br>10 | <br>Jednoznačné identifikační číslo dávky. |
| <br>6 | <br>„-„ | <br>1 | <br>Oddělovač. |
| <br>7 | <br>„dot“ nebo „odp“ | <br>3 | <br>Identifikace, zda se jedná o dotaz („dot“) nebo odpověď („odp“). |
| <br>8 | <br>„.xml“ | <br>4 | <br>Přípona indikující typ souboru. |

1\) Dotaz je zabalen do *SOAP* obálky s hlavičkou, která obsahuje metadata zprávy a pečeť. Má následující strukturu:

•

*SOAP-Envelope*

○ *SOAP-Header*

■

*Zprava*

■

*Signature*

○ *SOAP-Body*

■

*Davka*

•

*Dotaz* (kolekce)

○ *Dotazujici*

○ *DSubjekt*

2\) Odpověď je zabalena do SOAP obálky s hlavičkou, která obsahuje metadata zprávy a pečeť. Na každý dotaz je vytvořena právě jedna odpověď. Odpověď obsahuje tělo dotazu. Odpověď má následující strukturu:

•

*SOAP-Envelope*

○ *SOAP-Header*

■

*Zprava*

■

*Signature*

○ *SOAP-Body*

■

*Davka*

•

*Odpoved*(kolekce)

o *Dotaz*

■

*Dotazujici*

■

*Dsubjekt*

o *Odpovidajici*

o *DSubjekt*

o *Ucet*(0..n)

o *Chyba*(místo *DSubjekt*a *Ucet*)

**C) Obsah datové zprávy**

1\) Dotaz obsahuje prvky *Davka*, *Dotaz*, *Dotazujici* a *DSubjekt* ve struktuře podle části B. Každý prvek se skládá z atributů.

a) Prvek *Davka*

Jeden soubor může obsahovat dotaz na více subjektů. Prvek *Davka*obsahuje dotazy na jednotlivé subjekty.

| <br>**Prvek** | <br>**Atribut** | <br>**Popis** |
|---|---|---|
| <br>Davka | | <br>identifikace dávky |
| | <br>Id | <br>Identifikátor pro podpis – musí být „Davka“ |
| | <br>CisloDavky | <br>číslo dávky (dotazu) |
| | <br>Pocet | <br>počet dotazů/odpovědí v dávce |
| | <br>KodFU | <br>kód dotazujícího se orgánu pomoci v hmotné nouzi |
| | <br>JmenoFU | <br>název dotazujícího se orgánu pomoci v hmotné nouzi |
| | <br>KodBanky | <br>identifikační kód dotazovaného peněžního ústavu |
| | <br>JmenoBanky | <br>název dotazovaného peněžního ústavu |
| | <br>DatumCasDotazu | <br>datum a čas generování dotazu |
| | <br>CisloDavkyOdpovedi | <br>číslo odpovědi (pouze v odpovědi) |
| | <br>DatumCasOdpovedi | <br>datum a čas generování odpovědi (pouze v odpovědi) |

b) Prvek *Dotaz*

Prvek *Dotaz* obsahuje identifikaci osoby a identifikaci dotazujícího se.

Identifikace dotazu

| <br>**Prvek** | <br>**Atribut** | <br>**Popis** |
|---|---|---|
| <br>Dotaz | | |
| | <br>TypDotazu | <br>Uvede se "02" |
| | <br>KodDotazu | <br>Kód dotazu |

c) Prvek *Dotazujici*

Identifikace dotazující se osoby.

| <br>**Prvek** | <br>**Atribut** | <br>**Popis** |
|---|---|---|
| <br>Dotazujici | | |
| | <br>Jmeno | <br>Odpovědná osoba, jméno |
| | <br>Cislo | <br>Odpovědná osoba, identifikační číslo |

d) Prvek *DSubjekt*

Identifikace osoby, které se dotaz týká.

| <br>**Prvek** | <br>**Atribut** | <br>**Popis** |
|---|---|---|
| <br>DSubjekt | | |
| | <br>RC | <br>rodné číslo klienta |
| | <br>Typ | <br>Typ klienta |
| | <br>Jmeno | <br>Jméno |
| | <br>Ulice | <br>Ulice |
| | <br>Obec | <br>Obec |
| | <br>PSC | <br>Poštovní směrovací číslo |

2\) Odpověď obsahuje prvky *Davka*, *Odpoved*, *Dotaz*, *Dotazujici*, *DSubjekt*, *Odpovidajici*, *Ucet*a *Chyba*.

Prvky *Davka*, Dotaz, *Dotazujici*a *DSubjekt*jsou stejné jako v dotazu. Prvek *Dotaz*je kopií přijatého dotazu. Prvek *DSubjekt*v prvku *Odpoved*je tvořen z dat peněžního ústavu, ne kopií dotazu.

a) Prvek *Odpoved*

Prvek *Odpoved*obsahuje data o účtech osoby, které se dotaz týká, případně chybu, pokud peněžní ústav danou osobu nerozpozná.

| <br>**Prvek** | <br>**Atribut** | <br>**Popis** |
|---|---|---|
| <br>Odpoved | | <br>Identifikace odpovědi |
| | <br>KodDotazu | <br>Kód dotazu |

b) Prvek *Odpovidajici*

Identifikace pracovníka odpovědného za správnost a úplnost odpovědi na straně peněžního ústavu.

| <br>**Prvek** | <br>**Atribut** | <br>**Popis** |
|---|---|---|
| <br>Odpovidajici | | |
| | <br>Jmeno | <br>Jméno |
| | <br>Cislo | <br>Číslo pracovníka |

c) Prvek *Ucet*

Identifikace účtu. Jeden záznam pro každý jeden nalezený účet.

| <br>**Prvek** | <br>**Atribut** | <br>**Popis** |
|---|---|---|
| <br>Ucet | | |
| | <br>CisloUctu1 | <br>1. část čísla účtu |
| | <br>CisloUctu2 | <br>2. část čísla účtu |
| | <br>KodBanky | <br>Kód peněžního ústavu |
| | <br>SpecSymbolICS | <br>Specifický symbol |
| | <br>TypUctu | <br>Typ účtu |
| | <br>KodMeny | <br>Měna |
| | <br>Zustatek | <br>Zůstatek |
| | <br>Datum | <br>Den stanoveného zůstatku |

d) Prvek *Chyba*

Prvek *Chyba*se vytváří v případě chyby vzniklé při zpracování odpovědi.

| <br>**Prvek** | <br>**Atribut** | <br>**Popis** |
|---|---|---|
| <br>Chyba | | |
| | <br>Kod | <br>Chybový kód (následující tabulka) |
| | <br>Popis | <br>Text chyby |

V komunikaci mezi orgánem pomoci v hmotné nouzi a peněžním ústavem jsou rozpoznávány tyto chyby s těmito kódy:

| <br>**Chybový kód** | <br>**Chybová zpráva** | <br>**Komentář** |
|---|---|---|
| <br>-100 | <br>Chybný kód banky | <br>V headeru dotazu je chybný kód peněžního ústavu, který dotaz přijal. |
| <br>-101 | <br>Chybný autentikační kód | <br>Došlo k chybě při kontrole autentikačního kódu, resp. podpisu. |
| <br>-200 | <br>Chybný typ dotazu | <br>Typ dotazu je jiný než 01 / 02 / 03 / 04. |
| <br>-201 | <br>Chybí identifikace dotazujícího se subjektu | <br>XML element dot:Dotazujici chybí nebo obsahuje některé prázdné atributy. |
| <br>-300 | <br>Chybí identifikace klienta | <br>U dotazů typu 01 a 02 chybí element dot:DSubjekt nebo obsahuje pouze prázdné atributy. |
| <br>-303 | <br>Chybná identifikace klienta pomocí RČ | <br>U dotazů typu 01 a 02 element dot:DSubjekt obsahuje chybnou hodnotu atributu rodného čísla. |
| <br>-304 | <br>Nejednoznačná identifikace klienta prostřednictvím RČ | <br>U dotazů typu 01 a 02 je při generování odpovědi nalezeno více vlastníků (klientů) evidovaných pod jedním rodným číslem. |

3)Atributy prvků dotazu a odpovědi jsou vyplněny podle následujících pravidel:

| <br>**Prvek** | <br>**Atribut** | <br>**Max.<br>počet znaků** | <br>**Popis pole** |
|---|---|---|---|
| <br>Dotaz | <br>TypDotazu | <br>2 | <br>Typ dotazu, vždy vyplněno hodnotou “02”. |
| <br>Dotaz | <br>KodDotazu | <br>10 | <br>Jedinečný kód dotazu generovaný dotazujícím se orgánem pomoci v hmotné nouzi. |
| <br>Dotazujici,<br>Odpovidajici | <br>Cislo | <br>8 | <br>Identifikace odpovědné osoby, v dotazu číslo pracovníka orgánu pomoci v hmotné nouzi, v odpovědi identifikace pracovníka peněžního ústavu. |
| <br>Dotazujici,<br>Odpovidajici | <br>Jmeno | <br>40 | <br>Titul, jméno a příjmení dotazujícího se nebo odpovídajícího pracovníka. |
| <br>DSubjekt | <br>Typ | <br>1 | <br>Vždy vyplněno jako “F”, fyzická osoba. |
| <br>Dsubjekt | <br>ICO | <br>10 | <br>Není využíváno. |
| <br>Dsubjekt | <br>RC | <br>10 | <br>Rodné číslo bez lomítka, devítimístné rodné číslo zůstává na 9 znaků. |
| <br>Dsubjekt | <br>Jmeno | <br>40 | <br>Vyplněno pouze v odpovědi. |
| <br>Dsubjekt | <br>Ulice | <br>50 | <br>Vyplněno pouze v odpovědi. |
| <br>Dsubjekt | <br>Obec | <br>50 | <br>Vyplněno pouze v odpovědi. |
| <br>Dsubjekt | <br>PSC | <br>5 | <br>Vyplněno pouze v odpovědi. |
| <br>Ucet | <br>CisloUctu1 | <br>6 | <br>Nepovinné pole, je-li předčíslí rovno nule, není nutno jej uvádět. V předčíslí mohou být uvedeny úvodní nuly. Úvodní nuly jsou nevýznamové. Pole je variabilní délky. |
| <br>Ucet | <br>CisloUctu2 | <br>10 | <br>Základní části čísla účtu. Mohou být uvedeny úvodní nuly. Úvodní nuly jsou nevýznamové. Pole je variabilní délky. |
| <br>Ucet | <br>KodBanky | <br>4 | <br>Kód peněžního ústavu podle číselníku ČNB AP – 0001 s úvodními nulami. |
| <br>Ucet | <br>SpecSymbolCS | <br>max. 10 znaků | <br>Není využíváno. |
| <br>Ucet | <br>TypUctu | <br>1 | <br>Vyplní se hodnotou “B” pro běžný účet, “V” pro vkladový účet, “J” pro jiný účet a “X” pro chráněný účet. |
| <br>Ucet | <br>KodMeny | <br>3 | <br>ISO kód měny, ve které je veden účet. |
| <br>Ucet | <br>Zustatek | <br>15 | <br>V jednotkách dané měny, přičemž poslední 2 místa oddělená desetinnou čárkou jsou desetinná místa příslušné měnové jednotky; bez úvodních nul, záporný zůstatek se znaménkem minus. |
| <br>Ucet | <br>Datum | <br>10 | <br>Datum zůstatku na účtu. |

### Příloha č. 2

#### Specifikace komunikace mezi orgánem pomoci v hmotné nouzi a zaměstnavatelem a formát, obsah a struktura datové zprávy

**A)** **Specifikace způsobů odpovědi zaměstnavatele na výzvu orgánu pomoci v hmotné nouzi**

1\) Zaměstnavatel využívá pro odpověď na výzvu orgánu pomoci v hmotné nouzi tyto způsoby:

a) odeslání odpovědi doplněného XML souboru z datové schránky zaměstnavatele,

b) odeslání odpovědi prostřednictvím webového formuláře, nebo

c)odeslání odpovědi prostřednictvím přímého volání služby založené na standardu GovTalk.

2\) Specifikace způsobu odpovědi zaměstnavatele na výzvu orgánu pomoci v hmotné nouzi s využitím odeslání doplněného XML souboru z datové schránky zaměstnavatele:

a) Pro odeslání doplněného XML souboru se využije datová schránka zaměstnavatele nebo datová schránka osoby, kterou zaměstnavatel zmocní prostřednictvím elektronické služby „Správa plných mocí“ ePortálu České správy sociálního zabezpečení, a doplněný XML soubor se adresuje do datové schránky určené orgánem pomoci v hmotné nouzi ve výzvě.

b) Pro doplnění XML souboru je možné využít vlastní technické prostředky nebo volně dostupný online editor orgánu pomoci v hmotné nouzi.

3\) Specifikace způsobu odpovědi zaměstnavatele na výzvu orgánu pomoci v hmotné nouzi prostřednictvím webového formuláře, dostupného v odkazu uvedeném ve výzvě při využití webového formuláře vyžaduje autentizaci zaměstnavatele prostřednictvím Informačního systému datových schránek, nebo datovou schránkou osoby, kterou zaměstnavatel zmocní prostřednictvím elektronické služby „Správa plných mocí“ ePortálu České správy sociálního zabezpečení.

4\) Specifikace způsobu odpovědi zaměstnavatele na výzvu orgánu pomoci v hmotné nouzi prostřednictvím přímého volání služby založené na standardu GovTalk:

a) Autentizace a elektronický podpis dat pro službu je prováděn výhradně kvalifikovaným certifikátem registrovaným u České správy sociálního zabezpečení.

b) Pro podání prostřednictvím přímého volání služby se datová věta vloží do obálky ve formátu GovTalk verze 2.

c) Datová věta je součástí elementu Body ve formátu XML.

d) Struktura obálky, která je zveřejněna na internetových stránkách www.mpsv.cz ke dni odeslání odpovědi zaměstnavatele na výzvu orgánu pomoci v hmotné nouzi.

**B) Formát**

Odpověď zaměstnavatele je orgánem pomoci v hmotné nouzi přijímána výhradně ve formátu XML.

**C) Obsah a struktura datové zprávy**

1\) Obsah datové věty

| <br>**Atribut** | <br>**Typ** | <br>**Popis** |
|---|---|---|
| <br>UUID | <br>string | <br>Unikátní identifikátor výzvy. |
| <br>cisloJednaci | <br>string | <br>Číslo jednací výzvy k poskytnutí příjmů. |
| <br>rodneCislo | <br>string | <br>Rodné číslo zaměstnance. |
| <br>Jmeno, prijmeni | <br>string | <br>Jméno a příjmení zaměstnance. |
| <br>datumNarozeni | <br>Datum | <br>Datum narození zaměstnance. |
| <br>ikMPSV | <br>string | <br>Unikátní identifikátor zaměstnance. |
| <br>Prijmy | <br>kolekce | <br>Kolekce příjmů po jednotlivých měsících. |
| <br>vysePrijmuKodA1 | <br>int | <br>Příjmy ze závislé činnosti vykonávané v České republice (Příjmy ze závislé činnosti a funkční požitky uvedené v zákoně o daních z příjmů). |
| <br>vysePrijmuKodAB | <br>int | <br>Příjmy získané z náhrady mzdy (platu, odměny) za dobu prvních 14 dnů dočasné pracovní neschopnosti (karantény) podle § 192 odst. 2 zákoníku práce (kód ab). |
| <br>vysePrijmuKodA1Mena,<br>vysePrijmuKodABMena | <br>Měny, číselník | <br>Číselník měn, kódy podle normy ISO 4217. |
| <br>rok, mesic | <br>int | <br>Rok a měsíc, za který daný příjem náleží, podle výzvy. |
| <br>prijemOd, prijemDo | <br>Datum | <br>Data období, za které v daném roce a daném měsíci příjem náleží. |
| <br>bylZamestnancem | <br>boolean | <br>TRUE pokud byl alespoň část dotazovaného období zaměstnancem, jinak FALSE. |

2)Datové typy

| <br>Datum | <br>Textový řetězec data ve formátu RFC 3339, section 5.6, YYYY-MM-DD. |
|---|---|

3\) Číselníky

Měny – jako klíč číselníku Měny je využíván kód měny podle normy ISO 4217.

### Příloha č. 3

#### Specifikace komunikace mezi orgánem pomoci v hmotné nouzi a dodavatelem plynu nebo elektřiny a formát, obsah a struktura datové zprávy

**A) Specifikace způsobů odpovědi dodavatele plynu nebo elektřiny na výzvu orgánu pomoci v hmotné nouzi**

1\) Dodavatel plynu nebo elektřiny odešle odpověď na výzvu orgánu pomoci v hmotné nouzi jako JSON soubor ve formátu podle části B z datové schránky dodavatele plynu nebo elektřiny.

2\) Specifikace způsobu odpovědi dodavatele plynu nebo elektřiny na výzvu orgánu pomoci v hmotné nouzi s využitím odeslání JSON souboru ve formátu podle části B z datové schránky dodavatele plynu nebo elektřiny:

a) Pro odeslání JSON souboru se využije datová schránka dodavatele plynu nebo elektřiny.

b) Pro vytvoření JSON souboru dodavatel plynu nebo elektřiny využije vlastní technické prostředky.

**B) Formát**

Odpověď dodavatele plynu nebo elektřiny je orgánem pomoci v hmotné nouzi přijímána výhradně ve formátu JSON.

**C) Obsah a struktura datové zprávy**

1\) Obsah datové věty

| <br>**Pole** | <br>**Typ** | <br>**Popis** |
|---|---|---|
| <br>id | <br>string | <br>Id výzvy, na niž je odpovídáno. |
| <br>supplierId | <br>string | <br>Každý dodavatel plynu nebo elektřiny obdrží jednoznačný identifikátor od Ministerstva práce a sociálních věcí. |
| <br>Data | <br>array | <br>Pole záznamů s daty, 1 záznam obsahuje data pro 1 odběratele a 1 odběrné místo. |
| <br>Data/id | <br>string | <br>Bezvýznamový unikátní identifikátor záznamu, který byl součástí výzvy se žádostí o data. Musí být vrácen jako součást dat s náklady pro daného odběratele a odběrné místo. |
| <br>Data/client | <br>object | <br>Data odběratele. |
| <br>Data/client/clientId | <br>string | <br>Unikátní identifikátor odběratele v rámci systémů dodavatele plynu nebo elektřiny. Slouží hlavně pro případné řešení nestandardních situací, ve standardním procesu není nijak využito. |
| <br>Data/client/firstName | <br>string | <br>Jméno odběratele. |
| <br>Data/client/lastName | <br>string | <br>Příjmení odběratele. |
| <br>Data/client/dateOfBirth | <br>string | <br>Datum narození odběratele. |
| <br>Data/pointOfDelivery | <br>object | <br>Data odběrného místa. |
| <br>Data/pointOfDelivery/ean | <br>string | <br>Číslo odběrného místa elektřiny, pokud jde o elektřinu, jinak neuvedeno. |
| <br>Data/pointOfDelivery/eic | <br>string | <br>Číslo odběrného místa plynu, pokud jde o plyn, jinak neuvedeno. |
| <br>Data/pointOfDelivery/ruianId | <br>string | <br>Identifikátor adresy v RUIAN. |
| <br>Data/pointOfDelivery/commodity | <br>string,<br>enum | <br>Komodita. Typ komodity podle číselníku uvedeného v bodu 3. |
| <br>data/transactions | <br>array | <br>Částky pro požadované období podle výzvy. Typ částky podle číselníku uvedeného v bodu 3. |
| <br>data/transactions/month | <br>string | <br>Měsíc a rok, podle formátu ISO 8061 (YYYY-MM). |
| <br>Data/transactions /trType | <br>string,<br>enum | <br>Typ částky. Typ částky podle číselníku uvedeného v bodu 3. |
| <br>data/transactions/amount | <br>number | <br>Výše částky. |
| <br>Status | <br>string | <br>Dle číselníku Status uvedeného v bodu 3. Pokud je uveden status NOT_CLIENT, celá část “data” není uvedena. |

2\) Datové typy

| <br>month | <br>Textový řetězec data ve formátu ISO 8061 YYYY-MM. |
|---|---|

3\) Číselníky

Typ částek:

| <br>**Kód** | <br>**Typ částky** | <br>**Popis** |
|---|---|---|
| <br>P | <br>platba | <br>Platby od odběratele přijaté v daném měsíci.<br>Pokud je více plateb v daném měsíci, je uveden součet. Nezapočítávají se platby nebo části plateb použité na pokuty nebo jiné sankce, případně na jiné další účely, jako je například pronájem LED žárovek (tyto částky se odečtou od částky, kterou odběratel v daném měsíci poslal). |
| <br>Z | <br>záloha (od zákazníka) | <br>Zálohy nebo jejich část vyrovnané platbou vykázané v měsíci původní zálohy. |
| <br>ZZ | <br>předepsaná záloha | <br>Záloha předepsaná odběrateli bez ohledu na to, jaké jsou jeho skutečné uhrazené zálohy. |
| <br>PV | <br>vyúčtovaný přeplatek vrácený odběrateli | <br>Přeplatek z vyúčtování vrácený odběrateli. Je uveden v měsíci, kdy došlo k vrácení, to znamená odeslání platby. |
| <br>PZ | <br>přeplatek použitý na zálohu | <br>Přeplatek z vyúčtování použitý na úhradu zálohy. Je uveden v měsíci splatnosti zálohy. |
| <br>NZ | <br>zaplacený nedoplatek faktury nebo jeho část | <br>Platba od odběratele přijatá v daném měsíci na úhradu nedoplatku z vyúčtování.<br>Podle data přijetí platby (ne podle data splatnosti). Pokud má odběratel splátkový kalendář, uvede se příslušná částka též jako NZ v daném měsíci (NZ se tak rozloží do více měsíců). |

Typ komodity:

| <br>**Kód** | <br>**Typ komodity** |
|---|---|
| <br>E | <br>elektřina |
| <br>G | <br>plyn |

Status:

| <br>**Kód** | <br>**Popis** |
|---|---|
| <br>OK | <br>Nemusí být uveden, vše v pořádku. |
| <br>NOT_CLIENT | <br>Klient v žádné části požadovaného období nebyl majitelem daného odběrného místa. |
| <br>NOT_CLIENT_FULL_TIME | <br>Klient je/byl majitelem tohoto odběrného místa, ale ne pro celé požadované období – pro dané odběrné místo tedy mohou být data vrácena jen pro část požadovaného období. |
