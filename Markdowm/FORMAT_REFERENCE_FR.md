# Référence des formats de dépêches BELGA — Fil francophone

## Standard de base : IPTC 7901 Revision 5 (1995)

Spécification officielle : `iptc.org/std/IPTC7901/1.0/specification/7901V5.pdf`

Le format texte des dépêches BELGA est une variante du standard IPTC 7901
(International Press Telecommunications Council), utilisé par toutes les
agences de presse (AFP, Reuters, DPA, etc.) depuis les années 70.

> **Périmètre de ce document** : dépêches francophones uniquement (~1,96M sur
> 3,8M au total). Les dépêches néerlandophones (préfixe `NKBR`, code langue `N`)
> sont exclues. Les dépêches bilingues (`B`, `T`) sont mentionnées quand elles
> apparaissent sur le fil francophone.

---

## Les 4 formats du corpus

| Format | Années | Volume (FR) | Particularité |
|--------|--------|-------------|---------------|
| `.xml` (NewsML) | 1994–2026 | ~480k fichiers `FKBR*.xml` | 1 fichier = 1 dépêche, structuré |
| `.txt` individuel | 2002–2019 | ~800k fichiers `FKBR*_*.txt` | 1 fichier = 1 dépêche, en-tête IPTC 7901 |
| `.FRA` | 1995–2002 | ~1700 fichiers | 1 fichier = toutes les dépêches FR du jour, séparées par `./.` |
| `.txt` monobloc | 1996 | 313 fichiers `FKBR[date].txt` | 1 fichier = toutes les dépêches FR du jour (même format que `.FRA`) |

### Chronologie des transitions

| Période | Format principal | Notes |
|---------|-----------------|-------|
| 1994–1995 | xml seul | |
| **1996** | **xml + monoblocs txt** | `FKBR19960101.txt` — même contenu que les `.FRA` mais nommage différent |
| 1995–2001 | xml + `.FRA` en parallèle | Flux distincts (pas de doublons) |
| 2002/01–04 | xml + derniers `.FRA` | Derniers FRA en avril 2002 |
| 2002/06 | **Bascule vers .txt individuel** | txt + quelques xml sporadiques |
| 2003–2019/03 | .txt individuel dominant | Quelques xml sporadiques certains mois |
| 2019/04 | **Bascule vers xml** | |
| 2019/04–2026 | xml seul | Format NewsML moderne |

Les `.FRA` et `.xml` coexistent sans recouvrement : le fil télex (FRA) et
les fichiers XML individuels sont des flux de distribution différents.

### Monoblocs 1996 — cas particulier

En 1996, les agrégés quotidiens utilisent le nommage `FKBR[AAAAMMJJ].txt` au lieu
de `JJMMAA.FRA`. Le contenu est identique : horodatage télex, dépêches concaténées,
séparateurs `./.` + DTG.

Pour la période du **26 mars au 15 avril 1996**, certains monoblocs étaient trop
volumineux et ont été découpés en parties avec un suffixe alphabétique :

| Fichier | Parties | Taille partie A |
|---------|---------|-----------------|
| `FKBR19960328.txt` | A–K (11 parties) | ~1500 lignes |
| `FKBR19960414.txt` | A–J (10 parties) | ~1500 lignes |
| `FKBR19960329.txt` | A–J (10 parties) | ~1500 lignes |
| etc. | jusqu'à L max | dernière partie souvent courte (~50 lignes) |

Ces fichiers découpés coexistent avec les XML individuels (`FKBR199603280122_8110005.xml`,
etc.) dans les mêmes répertoires — ce sont les mêmes dépêches sous deux formes.

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

### Séparateur de dépêches (fichiers .FRA)

Les dépêches sont séparées par `./.\n` suivi d'un DTG. Chaque fichier
contient ~250 dépêches/jour.

### Exemple concret — dépêche sportive (310797.FRA)

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
- Le code langue (`F`, ou `B` pour les bilingues sur le fil FR)
- L'identifiant dépêche (`BELGA-0001` ou `BELGA-....`)
- Parfois des suffixes : initiales journaliste, `COR` (correctif), numéro

---

## Préfixes de service

Sur le fil francophone (~1,96M de dépêches) :

| Préfixe | Volume estimé | Signification |
|---------|---------------|---------------|
| **INT** | ~674k | Intérieur — actualité intérieure belge |
| **SPF** | ~532k (F) + ~93k (B) | Sport/Presse Francophone |
| **EXT** | ~605k | Extérieur — international |
| **BRF** | 11k | Brèves |
| **TTF** | 118 | Communiqués francophones (famille TT) |
| **SDA** | 205 | Service Diffusion Avis — avis de recherche (SGAP/police) |
| **FPB** | 83 | Fil Presse Belgique — communiqués UNS |
| **CMF** | 35 | Communiqués non rédactionnels |

Préfixes rares sur le fil FR (< 10 occurrences) : `BINT`, `BFR`.

> Note : les préfixes néerlandophones correspondants sont `BIN` (intérieur),
> `SPN` (sport), `BTL` (international), `BRN` (brèves). Ils apparaissent
> exclusivement dans les fichiers `NKBR`.

---

## Priorités

| Code | Niveau | Usage |
|------|--------|-------|
| **1** | Flash | Événement exceptionnel (mort chef d'État, attentat majeur) |
| **2** | Urgent / Alert | Breaking news |
| **3** | Normal | Standard — 96% du corpus |
| **4** | Différé | Background, features, communiqués de presse |

Exemple flash : `INT001 1 POL 0025 F BELGA-....`

---

## Codes langue sur le fil francophone

| Code | Signification | Notes |
|------|---------------|-------|
| **F** | Français | Très grande majorité |
| **B** | Bilingue | FR + NL dans le même texte ; fréquent années 90–2000, sur les services SPF (14%) et INT |
| **T** | Tweetalig (alertes bilingues) | Toujours priorité 2, toujours ALERT dans le titre, à partir de 2010 |
| **E** | English | Extrêmement rare (~22 occurrences), uniquement communiqués |

Les dépêches `B` et `T` se retrouvent dans des fichiers `FKBR` comme `NKBR` — elles ne sont pas
spécifiques à un fil. Dans les fichiers agrégés, les bilingues (`B`) apparaissent dans le `.FRA` *et*
le `.NED`.

---

## Catégories (rubriques) du fil francophone

### Actualité générale

| Code | Volume | Signification | Préfixes typiques |
|------|--------|---------------|-------------------|
| **GEN** | 1,16M | Général | INT, EXT, SPF |
| **POL** | ~300k (FR) | Politique | INT, EXT |
| **ECO** | ~200k (FR) | Économie | INT, EXT |
| **FIN** | ~18k (FR) | Finance / marchés | INT |
| **PRV** | ~18k (FR) | Provinciale (régional) | INT |
| **CLT** | ~3k (FR) | Culture | EXT |

> Note : `ALG` (Algemeen) est l'équivalent néerlandais de `GEN` ; `EUR` est
> quasi exclusivement néerlandais (service BTL).

### Sport

| Code | Volume | Signification | Préfixes typiques |
|------|--------|---------------|-------------------|
| **RES** | 139k | Résultats sportifs | SPF |
| **REB** | ~40k (FR) | Résultats sportifs belges | SPF |
| **RAN** | ~30k (FR) | Rankings / classements | SPF |
| **OLY** | ~10k (FR) | Jeux Olympiques | SPF |
| **HIP** | ~6k (FR) | Hippisme | SPF |
| **HFR** | 5k | Hippisme France (courses françaises) | SPF |
| **POD** | ~4k (FR) | Podium (résultats) | SPF |
| **SPO** | ~3k (FR) | Sport (général, brèves) | BRF |
| **MON** | ~2k (FR) | Mondial (Coupe du monde) | SPF |
| **TDF** | ~2k (FR) | Tour de France | SPF |
| **CDM** | 382 | Coupe du Monde (variante) | SPF |

> Note : `UIT` (Uitslagen) et `WED` (Wedstrijd) sont les équivalents
> néerlandais de `RES` et des catégories de compétition ; ils n'apparaissent
> pas sur le fil FR.

### Communiqués et spéciaux

| Code | Volume (FR) | Signification | Préfixes typiques |
|------|-------------|---------------|-------------------|
| **EMC** | ~1,5k | Communiqués non rédactionnels | SDA, CMF, TTF |
| **FFF** | 83 | Communiqués UNS (fil commercial) | FPB |

### Autres catégories (< 1000 occurrences, fil FR)

| Code | Volume | Signification probable |
|------|--------|----------------------|
| **PRE** | ~500 | Presse (revue de presse) |
| **EVE** | ~400 | Événements / agenda |
| **PRO** | ~270 | Programme (agenda sport) |
| **RSB** | ~220 | Résultats sportifs belges (variante) |
| **NAR** | 266 | Narration / éclairage |
| **TAS** | 265 | ? |
| **CLA** | 244 | Classements (variante de RAN) |
| **SEL** | 157 | Sélections (sport) |
| **BIL** | 150 | Bilingue (dépêches mixtes) |

---

## Slugline (IPTC 4.12)

Ligne 2 après l'en-tête. Mots-clés en majuscules séparés par `/`.
Hiérarchie thématique/géographique.

Exemples francophones :
- `FOOTBALL/`
- `RUSSIE/GB/`
- `EU/ ENVIRONNEMENT/`
- `EUROPE/COMEURO/ENERGIE/AGENDA/ATTENTION USERS/`
- `ATTENTION USERS/FOOTBALL/`
- `ATTENTION USERS/BELGASERVICE/PRESS/`

> Note : certaines sluglines sont bilingues dans les dépêches `B` :
> `KOERSEN/ COURS/ BEURS/ BOURSE/`

---

## Titre

Ligne 3. Peut contenir un indicateur de version entre parenthèses :
- aucun suffixe = première version
- `(2)`, `(3)` = mise à jour n°2, n°3
- `(3DER)` = version finale (`DER` = dernier)
- `(CORRECT)` ou `(RECTIFICATIF)` = correction
- `(1LEAD)` = premier chapeau

---

## Dateline

Format : `   VILLE JJ/MM (SOURCE(S)) = début du texte`

Sources les plus fréquentes :
BELGA (dominante), AFP (2e source), DPA, ATS, BLOOMBERG.

Sources composites : `(AFP-BELGA)`, `(AFP-DPA-REUTER)`, etc.

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

Format : `AAAAMMJJTHHMMSS`

Exemple : `20220211T045731` = 11 février 2022 à 04h57min31s.

---

## Noms de fichiers

| Type | Format du nom | Époque | Exemple |
|------|---------------|--------|---------|
| Agrégé quotidien | `JJMMAA.FRA` ou `JJMMAAA.FRA` | 1995–2002 | `310797.FRA`, `08042002.FRA` |
| Monobloc quotidien | `FKBR[AAAAMMJJ].txt` | 1996 | `FKBR19960101.txt` |
| Monobloc découpé | `FKBR[AAAAMMJJ][A-L].txt` | 1996 (mars–avril) | `FKBR19960328A.txt` |
| Txt individuel | `FKBR[datetime]_[id].txt` | 2002–2019 | `FKBR200706150920_141.txt` |
| XML individuel | `FKBR[datetime]_[id].xml` | 1994–2026 | `FKBR199406150000_10020940.xml` |

Préfixe `F` = français. `KBR` = identifiant archive (Koninklijke Bibliotheek).

> **Distinguer monobloc et individuel** : les fichiers txt individuels ont un
> underscore `_` dans le nom (`FKBR200706150920_141.txt`), les monoblocs n'en
> ont pas (`FKBR19960101.txt`).

> Les dépêches bilingues (`B`, `T`) peuvent se trouver dans des fichiers `FKBR`
> ou `NKBR` indifféremment. Dans les `.FRA` et monoblocs, les bilingues sont incluses.

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
        <HeadLine>Titre de la dépêche</HeadLine>
      </NewsLines>
      <DescriptiveMetadata>
        <Genre FormalName="1"/>
      </DescriptiveMetadata>
      <NewsComponent xml:lang="fr" Duid="10020940">
        <Role FormalName="Text"/>
        <NewsLines>
          <HeadLine>Titre de la dépêche</HeadLine>
          <CreditLine>BELGA</CreditLine>
          <KeywordLine>POLITIQUE/BELGIQUE</KeywordLine>
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
            <Property FormalName="City" Value="BRUXELLES"/>
          </Location>
        </DescriptiveMetadata>
        <NewsComponent Duid="10020941">
          <Role FormalName="Title"/>
          <ContentItem>
            <DataContent><![CDATA[Titre de la dépêche]]></DataContent>
          </ContentItem>
        </NewsComponent>
        <NewsComponent Duid="10020942">
          <Role FormalName="Lead"/>
          <ContentItem>
            <DataContent><![CDATA[BRUXELLES 15/06 (BELGA) = Corps...]]></DataContent>
          </ContentItem>
        </NewsComponent>
      </NewsComponent>
    </NewsComponent>
  </NewsItem>
</NewsML>
```

> Note : pas de `<NewsEnvelope>`, quotes simples dans la déclaration XML.
> Attention : certains XML classiques (1994) portent `xml:lang="en"` par erreur
> alors que le contenu est en français ou néerlandais.

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

| Valeur | Signification | Exemple |
|--------|---------------|---------|
| `AUTHOR` | Journaliste auteur | `<Party FormalName="TSA" Topic="AUTHOR"/>` |
| `EDITOR` | Relecteur / desk | `<Party FormalName="DAC" Topic="EDITOR"/>` |
| `CORRESPONDENT` | Correspondant externe (id `COR NNN`) | `<Party FormalName="COR 805" Topic="CORRESPONDENT"/>` |

> Attention : `COR NNN` dans le Creator XML est un **identifiant de correspondant**.
> Ne pas confondre avec le suffixe `COR NNN` de l'en-tête texte qui signifie
> « correctif de la dépêche n°NNN ».

### Label

Apparaît à partir de ~2019. Code de section/édition.

| Valeur | Volume | Signification probable |
|--------|--------|----------------------|
| `S1` | majoritaire | Section 1 (actualité principale ?) |
| `S3` | rare | Section 3 |
| `F1` | rare | ? |
| `R2` | rare | ? |

### Distribution

Toujours `Default` (~99,9%). Une seule occurrence de `B` dans le corpus.

### Update (attribut de `RevisionId`)

Toujours `"N"` dans le corpus. Les mises à jour sont identifiées par le numéro
de `RevisionId` (1, 2, 3…) et non par cet attribut.

### Balises toujours vides

Présentes dans les XML modernes (~2019+) mais systématiquement vides :
`Contributor/Party`, `SubjectCode`, `Property SubLocation`,
`NewsService` et `NewsProduct` (dans `NewsEnvelope`).

---

## Mapping vers NewsML

| Champ texte | Champ NewsML cible | Notes |
|-------------|-------------------|-------|
| Préfixe service (INT, SPF…) | `Property NewsService` | Enfant de `Property NewsPackage` |
| Préfixe + n° séquentiel (INT024) | `Property ForeignId` | Absent des XML pré-2009 |
| N° séquentiel (001) | `Property NewsObjectId` | ID numérique unique |
| Priorité (1–4) | `Property Priority` | |
| Catégorie (GEN, POL…) | `Property NewsProduct` | Enfant de `Property NewsPackage` |
| Nombre de mots | aucun équivalent direct | `SizeInBytes` = taille en octets |
| Langue (F/B) | `xml:lang` (fr) | |
| ID dépêche | `NewsItemId` | |
| Slugline | `KeywordLine` | |
| Titre | `HeadLine` | |
| Ville dateline | `Location/Property City` | |
| Source(s) dateline | `Source/Party` | |
| Corps | `DataContent` | Découpé en Title, Lead, Body via `Role FormalName` |
| DTG | `FirstCreated` / `DateAndTime` | |
| Initiales journaliste | `Creator/Party` | `Topic="AUTHOR"`, `"EDITOR"` ou `"CORRESPONDENT"` |
| Version (2), (3DER) | `RevisionId` | `Update` toujours `"N"` |
