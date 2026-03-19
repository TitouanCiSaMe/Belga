# Référence des formats de dépêches BELGA

## Standard de base : IPTC 7901 Revision 5 (1995)

Spécification officielle : `iptc.org/std/IPTC7901/1.0/specification/7901V5.pdf`

Le format texte des dépêches BELGA est une variante du standard IPTC 7901
(International Press Telecommunications Council), utilisé par toutes les
agences de presse (AFP, Reuters, DPA, etc.) depuis les années 70.

---

## Les 3 formats du corpus

| Format | Années | Volume | Particularité |
|--------|--------|--------|---------------|
| `.xml` (NewsML) | 1994–2026 | ~2M fichiers | 1 fichier = 1 dépêche, structuré |
| `.txt` | 2002–2019 | ~3,2M fichiers | 1 fichier = 1 dépêche, en-tête IPTC 7901 |
| `.FRA` / `.NED` | 1995–2002 | ~3400 fichiers | 1 fichier = toutes les dépêches du jour, séparées par `./.` |

### Chronologie des transitions

| Période | Format principal | Notes |
|---------|-----------------|-------|
| 1994 | xml seul | |
| 1995–2001 | xml + `.FRA`/`.NED` en parallèle | Flux distincts (pas de doublons) |
| 2002/01–05 | xml + derniers FRA/NED | Derniers FRA/NED en avril 2002 |
| 2002/06 | **Bascule vers .txt** | txt + quelques xml sporadiques |
| 2003–2019/03 | .txt dominant | Quelques xml sporadiques certains mois |
| 2019/04 | **Bascule vers xml** | |
| 2019/04–2026 | xml seul | Format NewsML moderne |

Les `.FRA`/`.NED` et `.xml` coexistent sans recouvrement : le fil télex (FRA/NED) et
les fichiers XML individuels sont des flux de distribution différents.

---

## Structure d'une dépêche texte (IPTC 7901)

```
[31-JUL-97  00:00]                         ← horodatage session télex (optionnel)

SPF001 3 RES 0070 F BELGA-0001             ← ligne d'en-tête
FOOTBALL/                                   ← slugline (mots-clés)
Ligue des champions - résultats (3DER)      ← titre

   BRUXELLES 23/07 (AFP-DPA-REUTER) =      ← dateline
Corps de la dépêche...                      ← corps

./.CVN                                      ← fin + initiales journaliste
310001 JUL 97                               ← DTG (Date-Time Group)
```

### Séparateur de dépêches (fichiers .FRA/.NED)

Les dépêches sont séparées par `./.\n` suivi d'un DTG. Chaque fichier
contient ~250 dépêches/jour.

### Exemple concret — dépêche sportive FR (310797.FRA)

```
SPF001 3 RES 0070 F BELGA-0001
FOOTBALL/
Ligue des champions - 1er tour qualification retour: résultats (3DER)


   BRUXELLES 23/07 (AFP-DPA-REUTER) = Dernier résultat des matches
retour du 1er tour de qualification de la Ligue des champions
1997-98, disputés mercredi:
                                                             Aller
   IA Akranes (Isl) - (+) FC Kosice (Svq)               0-1   0-3

   NDLR: Les clubs précédés du signe (+) sont qualifiés pour le 2e
tour de qualification

./.CVN

./.
310001 JUL 97
```

### Exemple concret — dépêche avec correctif (310797.FRA)

```
INT001 3 GEN 0091 F BELGA-0031 COR 703
DIVERS/
Il perd et sa voiture et la recette du match ...

   ROCHEFORT 31/07 (BELGA) = C'est en rentrant chez lui à Rochefort
ce jeudi matin vers 1 h que l'un des responsables du Football Club de
Rochefort a été agressé par deux individus armés et portant cagoule.
   Sous la menace de leur arme et après l'avoir molesté, les
malandrins ont obligé ce responsable à leur remettre la recette du
match Rochefort-Standard qui s'était déroulé dans la soirée ainsi que
les clés de sa voiture.
./.
310100 JUL 97
```

> Note : le `COR 703` dans l'en-tête indique un correctif. `703` est probablement
> un identifiant interne de la dépêche originale.

### Exemple concret — dépêche néerlandaise (310797.NED)

```
SPN001 3 UIT 0348 N BELGA-0002
VOETBAL/
Champions League (2)

   BRUSSEL 31/07 (AFP) - De uitslagen voor de eerste
kwalificatieronde om de Champions League 1997-98:

                                                      heen terug
    MARIBOR BRANIK (Slo) - Derry City (N-I)           2-0  1-0
    IA Akranes (Ijs) - FC KOSICE (Svk)                0-1  0-3
    FC CROATIA ZAGREB (Kro) - Partizan Belgrado (Joe) 0-1  5-0

./.
310001 JUL 97
```

### Exemple concret — fichier .txt individuel (2007)

Fichier : `FKBR200706150920_141.txt`

```
EXT010 3 GEN 0336 F BELGA-0102
RUSSIE/GB/
Affaire Litvinenko: le FSB ouvre une enquête pour espionnage

   MOSCOU 15/06 (AFP) = Les services spéciaux russes (FSB, ex-KGB) ont
ouvert une enquête pour espionnage sur la base des déclarations du Russe
Andreï Lougovoï, principal suspect dans l'enquête sur le meurtre de
l'ex-agent Alexandre Litvinenko, a annoncé vendredi le FSB cité par les
agences de presse russes.
./.
150920 JUN 07
```

---

## Ligne d'en-tête — décodage champ par champ

```
SPF001 3 RES 0070 F BELGA-0001
│  │   │  │   │   │    │
│  │   │  │   │   │    └─ Identifiant dépêche (IPTC 4.10 : champ optionnel libre)
│  │   │  │   │   └────── Langue (IPTC 4.10 : champ optionnel, convention BELGA)
│  │   │  │   └────────── Nombre de mots approximatif (IPTC 4.8)
│  │   │  └────────────── Catégorie/rubrique (IPTC 4.6)
│  │   └───────────────── Priorité (IPTC 4.4)
│  └───────────────────── Numéro séquentiel du jour, repart à 001 chaque jour
└──────────────────────── Identifiant de service (IPTC 4.2)
```

Référence spec : Section 4 de IPTC 7901 Rev. 5.

### Champ optionnel (IPTC 4.10)

La spec autorise jusqu'à 50 caractères libres. BELGA y place :
- Le code langue (`F`, `N`, `B`, `T`)
- L'identifiant dépêche (`BELGA-0001` ou `BELGA-....`)
- Parfois des suffixes : initiales journaliste, `COR` (correctif), `DCM`, numéro

---

## Préfixes de service

Analysés sur 3,8M de lignes d'en-tête.

| Préfixe | Volume | Langue | Signification |
|---------|--------|--------|---------------|
| **BIN** | 792k | N (98%) | Binnenland — actualité intérieure NL |
| **INT** | 709k | F (95%) | Intérieur — actualité intérieure FR |
| **SPF** | 665k | F (80%) + B (14%) | Service Presse Francophone (dont sport) |
| **EXT** | 618k | F (98%) | Extérieur / International FR |
| **SPN** | 597k | N (76%) + B (16%) | Service Presse Néerlandophone (dont sport) |
| **BTL** | 436k | N (99%) | Buitenland — international NL |
| **BRN** | 12k | N | Brèves NL |
| **BRF** | 11k | F | Brèves FR |
| **CMN/CMF** | ~50 | N / F | Communications (rares) |

Préfixes marginaux (<10 occurrences) : `SPC`, `IBIN`, `BFR`, `INR`, `SPE`, `VLR`, `BINT`, `PF`, `ERD`.

---

## Priorités

BELGA utilise une échelle **1–4** (la spec IPTC autorise 1–6, mais 5 et 6 sont absents du corpus).

| Code | Niveau | Volume | Usage |
|------|--------|--------|-------|
| **1** | Flash | 211 | Événement exceptionnel |
| **2** | Urgent/Alert | 140 763 | Breaking news |
| **3** | Normal | 3 701 665 | Standard (96% du corpus) |
| **4** | Différé | 1 337 | Background, features |

---

## Codes langue

Convention propriétaire BELGA (dans le champ optionnel IPTC 4.10).

| Code | Langue | Volume | Notes |
|------|--------|--------|-------|
| **F** | Français | 1,96M | |
| **N** | Néerlandais | 1,80M | |
| **B** | Bilingue | 48k | Usage classique (années 90–2000) |
| **T** | Tweetalig (bilingue alertes) | 36k | Alertes bilingues, toujours priorité 2, apparaît à partir de 2010 |

### Langue T — détail

Les dépêches `T` sont des **ALERTs courtes publiées simultanément dans les deux langues**.
Caractéristiques : toujours priorité 2, toujours `ALERT` ou `ALERT -` dans le slugline
ou le titre, corps mélangé FR/NL. Volume en croissance (281 en 2010 → 1077 en 2019).

---

## Catégories (rubriques)

| Code | Volume | Signification | Préfixes typiques |
|------|--------|---------------|-------------------|
| **GEN** | 1,16M | Général | INT, EXT, SPF |
| **ALG** | 1,03M | Algemeen (général NL) | BIN, BTL, SPN |
| **POL** | 588k | Politique | INT, EXT, BTL |
| **ECO** | 427k | Économie | BIN, INT, BTL, EXT |
| **UIT** | 173k | Uitslagen (résultats sportifs NL) | SPN |
| **RES** | 139k | Résultats sportifs FR | SPF |
| **REB** | 79k | Résultats sportifs belges | SPF, SPN |
| **RAN** | 61k | Rankings/classements | SPF, SPN |
| **FIN** | 36k | Finance/marchés | BIN, INT |
| **PRV** | 35k | Provinciale (régional) | BIN, INT |
| **EUR** | 26k | Europe | BTL |
| **OLY** | 20k | Jeux Olympiques | SPF, SPN |
| **HIP** | 12k | Hippisme | SPF, SPN |
| **POD** | 8k | Podium (sport) | SPN |
| **CLT** | 6k | Culture | EXT, BTL |
| **SPO** | 6k | Sport (général) | BRF, BRN |
| **HFR** | 5k | ? | |
| **MON** | 4k | Mondial | SPF, SPN |
| **TDF** | 4k | Tour de France | SPF, SPN |
| **WED** | 3k | Wedstrijd (compétition NL) | SPN |

---

## Slugline (IPTC 4.12)

Ligne 2 après l'en-tête. Mots-clés en majuscules séparés par `/`.
Hiérarchie thématique/géographique.

Exemples :
- `FOOTBALL/`
- `KOERSEN/ COURS/ BEURS/ BOURSE/` (bilingue)
- `BEDRIJVEN/ZWITSERLAND/VS/GERECHT/AGENDA/`
- `EU/ ENVIRONNEMENT/`
- `WIELRENNEN/TOUR DE FRANCE/ALERT/`

---

## Titre

Ligne 3. Peut contenir un indicateur de version entre parenthèses :
- aucun suffixe = première version
- `(2)`, `(3)` = mise à jour n°2, n°3
- `(3DER)` = version finale (`DER` = dernier)
- `(CORRECT)` ou `(RECTIFICATIF)` = correction

---

## Dateline

Format : `   VILLE JJ/MM (SOURCE(S)) = début du texte`

Sources les plus fréquentes (1997) :
BELGA (40k), AFP (24k), REUTER (4k), ANP (585), DPA (472), UPI (173), ATS (164).

Sources composites : `AFP-REUTER`, `AFP-BELGA`, `ANP-BELGA`, etc.

---

## Fin de dépêche

### Marqueur de fin
`./.` suivi optionnellement des initiales du journaliste : `./.CVN`, `./.LME`

Ou bien les initiales sur la dernière ligne du corps : `VDH/FUL/`
(auteur/éditeur de desk, abréviations de noms de famille).

### DTG (Date-Time Group) — IPTC Section 6.2

Format : `JJHHMM MOIS AA`

Exemple : `310001 JUL 97` = 31 juillet 1997 à 00h01.

- 2 premiers chiffres = jour du mois
- 4 chiffres suivants = HHMM (heure, minute)
- Mois en anglais abrégé (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC)
- Année sur 2 chiffres

### Horodatage XML — ISO 8601 basique

Dans les fichiers XML, tous les timestamps (`DateAndTime`, `FirstCreated`,
`ThisRevisionCreated`, `DateId`, `ValidationDate`) utilisent le format
ISO 8601 sans séparateurs :

Format : `AAAAMMJJTHHMMSS`

```
20220211T045731
││││││││ ││││││
││││││││ ││││└└─ secondes (SS)
││││││││ ││└└─── minutes  (MM)
││││││││ └└───── heures   (HH)
││││││││
││││└└└└──────── jour     (JJ)
││└└──────────── mois     (MM)
└└────────────── année    (AAAA)
```

Exemple : `20220211T045731` = 11 février 2022 à 04h57min31s.

Le `T` est le séparateur standard ISO 8601 entre date et heure.
C'est l'équivalent numérique du DTG texte (`310001 JUL 97`).

---

## Noms de fichiers

### `.FRA` / `.NED`
Format : `JJMMAA.FRA` ou `JJMMAAA.FRA` (ex: `310797.FRA`, `08042002.FRA`)

### `.txt`
Format : `XKBR[datetime]_[id].txt`
- `F` = français, `N` = néerlandais
- `KBR` = identifiant archive (Koninklijke Bibliotheek ?)
- datetime = `AAAAMMJJHHMM`
- id = identifiant numérique unique

### `.xml`
Même convention que `.txt` : `FKBR[datetime]_[id].xml`

---

## Exemples XML

### XML classique (1994) — sans `NewsEnvelope`

Fichier : `FKBR199406150000_10020940.xml`

```xml
<?xml version='1.0' encoding='UTF-8'?>
<NewsML>
  <Catalog Href="http://www.belga.be/dtd/BelgaCatalog.xml"/>
  <NewsItem>
    <Identification>
      <NewsIdentifier>
        <ProviderId>belga.be</ProviderId>
        <DateId>19940615T000000</DateId>
        <NewsItemId>10020931</NewsItemId>
        <RevisionId PreviousRevision="0" Update="N">1</RevisionId>
        <PublicIdentifier>urn:newsml:www.belga.be:10020931:1N</PublicIdentifier>
      </NewsIdentifier>
    </Identification>
    <NewsManagement>
      <NewsItemType FormalName="NEWS"/>
      <FirstCreated>19940615T000000</FirstCreated>
      <ThisRevisionCreated>19940615T000000</ThisRevisionCreated>
      <Status FormalName="USABLE"/>
    </NewsManagement>
    <NewsComponent Duid="10020931">
      <NewsLines>
        <HeadLine>Valsmunter veroordeeld</HeadLine>
      </NewsLines>
      <DescriptiveMetadata>
        <Genre FormalName="1"/>
      </DescriptiveMetadata>
      <NewsComponent xml:lang="en" Duid="10020940">
        <Role FormalName="Text"/>
        <NewsLines>
          <HeadLine>Valsmunter veroordeeld</HeadLine>
          <CreditLine>BELGA</CreditLine>
          <KeywordLine>GERECHT</KeywordLine>
        </NewsLines>
        <AdministrativeMetadata>
          <Source>
            <Party FormalName="belga"/>
          </Source>
          <Property FormalName="NewsPackage">
            <Property FormalName="NewsService" Value="NEWS"/>
            <Property FormalName="NewsProduct" Value="UNKNOWN"/>
          </Property>
          <Property FormalName="NewsObjectId" Value="10020940"/>
          <Property FormalName="Priority" Value="3"/>
          <Property FormalName="Distribution" Value="Default"/>
        </AdministrativeMetadata>
        <DescriptiveMetadata>
          <Location>
            <Property FormalName="City" Value="GENT"/>
          </Location>
        </DescriptiveMetadata>
        <NewsComponent Duid="10020941">
          <Role FormalName="Title"/>
          <ContentItem>
            <DataContent><![CDATA[Valsmunter veroordeeld]]></DataContent>
          </ContentItem>
        </NewsComponent>
        <NewsComponent Duid="10020942">
          <Role FormalName="Lead"/>
          <ContentItem>
            <DataContent><![CDATA[GENT 15/06 (belga) = De correctionele
rechtbank van Gent veroordeelde woensdag Andries S. (38) uit
Sint-Niklaas tot een gevangenisstraf van 18 maanden...]]></DataContent>
          </ContentItem>
        </NewsComponent>
      </NewsComponent>
    </NewsComponent>
  </NewsItem>
</NewsML>
```

> Note : pas de `<NewsEnvelope>`, quotes simples dans la déclaration XML,
> `xml:lang="en"` erroné (devrait être `nl`). Typique du format classique 1994–2010.

### XML moderne (2025) — avec `NewsEnvelope`

Fichier : `FKBR202503151445_d2e02e3b-1331-4c17-a363-2bd743a27c3b.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<NewsML>
  <Catalog Href="http://www.belga.be/dtd/BelgaCatalog.xml"/>
  <NewsEnvelope>
    <DateAndTime>20250315T144554</DateAndTime>
    <NewsService FormalName=""/>
    <NewsProduct FormalName=""/>
  </NewsEnvelope>
  <NewsItem>
    <Identification>
      <NewsIdentifier>
        <ProviderId>belga.be</ProviderId>
        <DateId>20250315T143325</DateId>
        <NewsItemId>1103465679</NewsItemId>
        <RevisionId PreviousRevision="0" Update="N">4</RevisionId>
        <PublicIdentifier>urn:newsml:www.belga.be:67d584...:4N</PublicIdentifier>
      </NewsIdentifier>
    </Identification>
    <NewsManagement>
      <NewsItemType FormalName="NEWS"/>
      <FirstCreated>20250315T143325</FirstCreated>
      <ThisRevisionCreated>20250315T144554</ThisRevisionCreated>
      <Status FormalName="USABLE"/>
    </NewsManagement>
    <NewsComponent Duid="1103465679" xml:lang="fr">
      <NewsLines>
        <HeadLine>Le président angolais appelle à un
        cessez-le-feu à minuit en RDC</HeadLine>
      </NewsLines>
      <NewsComponent Duid="1103465679" xml:lang="fr">
        <Role FormalName="Text"/>
        <NewsLines>
          <HeadLine>Violences dans l'est de la RDC - Le président
          angolais appelle à un cessez-le-feu...</HeadLine>
          <CreditLine>BELGA</CreditLine>
          <KeywordLine>VIOLENCE/RDC/ANGOLA</KeywordLine>
        </NewsLines>
        <!-- AdministrativeMetadata, DescriptiveMetadata, etc. -->
        <NewsComponent xml:lang="fr">
          <Role FormalName="Lead"/>
          <ContentItem>
            <DataContent><![CDATA[Le contenu du chapeau...]]></DataContent>
          </ContentItem>
        </NewsComponent>
        <NewsComponent xml:lang="fr">
          <Role FormalName="Body"/>
          <ContentItem>
            <DataContent><![CDATA[Le corps de la dépêche...]]></DataContent>
          </ContentItem>
        </NewsComponent>
      </NewsComponent>
    </NewsComponent>
  </NewsItem>
</NewsML>
```

> Note : `NewsEnvelope` présent, `xml:lang="fr"` correct, `NewsItemId` numérique
> long (compteur global), `RevisionId=4` (4e révision de la dépêche).

---

## Métadonnées propres au XML

Certains champs n'existent que dans les fichiers XML et n'ont pas d'équivalent dans le format texte.

### Genre

| Valeur | Époque | Signification |
|--------|--------|---------------|
| `""` (vide) | Toutes | Valeur par défaut (majorité des dépêches) |
| `"1"` | 1994–~2010 | Format classique — probablement « actualité courante » |
| `"CURRENT"` | ~2019+ | Format moderne — même signification que `"1"` |

### Creator — attribut `Topic`

Le `Topic` sur `Creator/Party` distingue trois rôles :

| Valeur | Signification | Exemple |
|--------|---------------|---------|
| `AUTHOR` | Journaliste auteur | `<Party FormalName="TSA" Topic="AUTHOR"/>` |
| `EDITOR` | Relecteur / desk | `<Party FormalName="DAC" Topic="EDITOR"/>` |
| `CORRESPONDENT` | Correspondant externe (identifiant `COR NNN`) | `<Party FormalName="COR 805" Topic="CORRESPONDENT"/>` |

> Note : `COR NNN` dans le Creator XML est un **identifiant de correspondant**, pas un
> correctif. Ne pas confondre avec le suffixe `COR NNN` de l'en-tête texte qui signifie
> « correctif de la dépêche n°NNN ».

### Label

Apparaît à partir de ~2019. Code de section/édition.

| Valeur | Volume | Signification probable |
|--------|--------|----------------------|
| `S1` | majoritaire | Section 1 (actualité principale ?) |
| `S3` | rare | Section 3 |
| `F1` | rare | ? |
| `R2` | rare | ? |

Exemple : `<Property FormalName="Label" Value="S1"/>`

### Distribution

| Valeur | Volume | Notes |
|--------|--------|-------|
| `Default` | ~99,9% | Distribution standard |
| `B` | 1 occurrence | Distribution restreinte ? |

### Update (attribut de `RevisionId`)

Toujours `"N"` dans le corpus BELGA. La spec NewsML prévoit aussi `"U"` (update),
mais BELGA ne l'utilise pas — les mises à jour sont identifiées par le numéro
de `RevisionId` (1, 2, 3…) et non par cet attribut.

### Balises toujours vides

Les balises suivantes sont présentes dans les XML modernes (~2019+) mais
systématiquement vides dans tout le corpus :

| Balise | Contexte |
|--------|----------|
| `Contributor/Party` | `AdministrativeMetadata` — contributeur externe (jamais renseigné) |
| `SubjectCode` | `DescriptiveMetadata` — code sujet IPTC (jamais renseigné) |
| `Property SubLocation` | `Location` — sous-localisation (jamais renseignée) |
| `NewsService` / `NewsProduct` (dans `NewsEnvelope`) | Doublons des valeurs dans `NewsPackage`, toujours vides dans l'enveloppe |

---

## Mapping vers NewsML

| Champ texte | Champ NewsML cible | Notes | Source |
|-------------|-------------------|-------|--------|
| Préfixe service (SPF, BIN...) | `Property NewsService` | Enfant de `Property NewsPackage` | En-tête, position 1 |
| Préfixe + n° séquentiel (INT024) | `Property ForeignId` | Reconstitution exacte du code IPTC texte (absent des XML pré-2009) | En-tête, position 1 |
| N° séquentiel (001) | `Property NewsObjectId` | ID numérique unique, pas le séquentiel du jour à proprement parler | En-tête, position 1 |
| Priorité (1–4) | `Property Priority` | | En-tête, position 2 |
| Catégorie (GEN, POL...) | `Property NewsProduct` | Enfant de `Property NewsPackage`. `Genre` existe mais quasi toujours vide (`""` ou `"1"`) | En-tête, position 3 |
| Nombre de mots | aucun équivalent direct | `SizeInBytes` = taille en octets de chaque composant (Title, Lead, Body), pas le nombre de mots global. `Property EditorialInfo` (1994 uniquement) était probablement le vrai réceptacle | En-tête, position 4 |
| Langue (F/N/B/T) | `xml:lang` (fr/nl) | | En-tête, position 5 |
| ID dépêche | `NewsItemId` | | En-tête, position 6 ou nom fichier |
| Slugline | `KeywordLine` | | Ligne 2 |
| Titre | `HeadLine` | | Ligne 3 |
| Ville dateline | `Location/Property City` | | Dateline |
| Source(s) dateline | `Source/Party` | | Dateline `(AFP-BELGA)` |
| Corps | `DataContent` | Découpé en composants Title, Lead, Body via `Role FormalName` | Corps |
| DTG | `FirstCreated` / `DateAndTime` | | Après `./.` |
| Initiales journaliste | `Creator/Party` | `Topic="AUTHOR"`, `"EDITOR"` ou `"CORRESPONDENT"` (voir section Métadonnées XML) | Avant DTG |
| Version (2), (3DER) | `RevisionId` | `Update` toujours `"N"` — le numéro de révision porte l'info | Parenthèses dans le titre |
