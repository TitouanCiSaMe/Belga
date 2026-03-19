# Dictionnaire des champs — Dépêches BELGA (fil francophone)

Référence des valeurs observées sur le fil francophone (~1,96M de dépêches, 1994–2026).
Les volumes marqués `~` sont des estimations basées sur la répartition linguistique du corpus complet.

---

## 1. Ligne d'en-tête — structure

```
SPF001 3 RES 0070 F BELGA-0001 COR 703
│  │   │  │   │   │    │        │    │
│  │   │  │   │   │    │        │    └─ Réf. dépêche originale (si correctif)
│  │   │  │   │   │    │        └────── Suffixe (COR, initiales, BELGASPORTS…)
│  │   │  │   │   │    └─────────────── Identifiant dépêche
│  │   │  │   │   └──────────────────── Langue
│  │   │  │   └──────────────────────── Nombre de mots (approximatif)
│  │   │  └──────────────────────────── Catégorie / rubrique
│  │   └─────────────────────────────── Priorité
│  └─────────────────────────────────── N° séquentiel du jour (repart à 001)
└────────────────────────────────────── Préfixe de service
```

---

## 2. Préfixes de service

### Principaux

| Préfixe | Volume estimé | Signification | Exemple |
|---------|---------------|---------------|---------|
| **INT** | ~674k | Intérieur — actualité intérieure belge | `INT136 3 GEN 0043 F BELGA-0666` |
| **SPF** | ~532k (F) + ~93k (B) | Sport/Presse Francophone | `SPF001 3 RES 0070 F BELGA-0001` |
| **EXT** | ~605k | Extérieur — international | `EXT059 3 POL 0304 F BELGA-0356` |
| **BRF** | 11k | Brèves | `BRF001 3 GEN 0123 F BELGA-....` |

### Secondaires

| Préfixe | Volume | Signification | Exemple |
|---------|--------|---------------|---------|
| **TTF** | 118 | Communiqués francophones (famille TT) | `TTF312 4 EMC 0690 F` |
| **SDA** | 205 | Service Diffusion Avis — avis de recherche (SGAP/police) | `SDA241 4 EMC 0183 F` |
| **FPB** | 83 | Fil Presse Belgique — communiqués UNS (Universal News Services) | `FPB603 4 FFF 0355 F` |
| **CMF** | 35 | Communiqués non rédactionnels | `CMF001 3 EMC 0130 F BELGA-0046 C` |

### Rares (< 10 occurrences)

| Préfixe | Volume | Signification | Exemple |
|---------|--------|---------------|---------|
| **CMQ** | 4 | Communiqués (variante) | `CMQ001 4 EMC 0063 F` |
| **BINT** | 1 | Buitenland-Intérieur (hybride) | `BINT007 3 GEN 0351 F BELGA-....` |
| **BFR** | 2 | Brèves France (?) | `BFR015 2 GEN 0192 F BELGA-....` |

> Note : les équivalents néerlandophones sont `BIN` (intérieur, 792k), `SPN`
> (sport, 597k), `BTL` (international, 436k), `BRN` (brèves, 12k). Ils
> apparaissent exclusivement dans les fichiers `NKBR`.

---

## 3. Priorités

| Code | Niveau | Usage | Exemple |
|------|--------|-------|---------|
| **1** | Flash | Événement exceptionnel (mort chef d'État, attentat majeur) | `INT001 1 POL 0025 F BELGA-....` |
| **2** | Urgent / Alert | Breaking news | `INT044 2 POL 0123 F BELGA-.... BPE` |
| **3** | Normal | Standard — 96% du corpus | `EXT059 3 POL 0304 F BELGA-0356` |
| **4** | Différé | Background, features, communiqués de presse | `TTF312 4 EMC 0690 F` |

---

## 4. Catégories (rubriques)

### Actualité générale

| Code | Volume | Signification | Préfixes typiques | Exemple |
|------|--------|---------------|-------------------|---------|
| **GEN** | 1,16M | Général | INT, EXT, SPF | `INT136 3 GEN 0043 F BELGA-0666` |
| **POL** | ~300k | Politique | INT, EXT | `EXT059 3 POL 0304 F BELGA-0356` |
| **ECO** | ~200k | Économie | INT, EXT | `INT003 3 ECO 0079 F BELGA-0058` |
| **FIN** | ~18k | Finance / marchés | INT | `EXT002 3 FIN 0284 F BELGA-0003` |
| **PRV** | ~18k | Provinciale (régional) | INT | `INT082 2 PRV 0638 B BELGA-0401` |
| **CLT** | ~3k | Culture | EXT | `EXT051 2 CLT 0485 F BELGA-0266` |

> Note : `ALG` (Algemeen) est l'équivalent NL de `GEN` (1,03M dépêches).
> `EUR` est quasi exclusivement NL (service BTL).

### Sport

| Code | Volume | Signification | Préfixes typiques | Exemple |
|------|--------|---------------|-------------------|---------|
| **RES** | 139k | Résultats sportifs | SPF | `SPF001 3 RES 0070 F BELGA-0001` |
| **REB** | ~40k | Résultats sportifs belges | SPF | `SPF044 3 REB 0088 B BELGA-0209` |
| **RAN** | ~30k | Rankings / classements | SPF | `SPF017 3 RAN 0152 B BELGA-0107` |
| **OLY** | ~10k | Jeux Olympiques | SPF | `SPF017 3 OLY 0509 F BELGA-0318` |
| **HIP** | ~6k | Hippisme (général) | SPF | `SPF059 3 HIP 0128 F BELGA-0580 TFX` |
| **HFR** | 5k | Hippisme France (courses françaises) | SPF | `SPF057 3 HFR 0123 F BELGA-....` |
| **POD** | ~4k | Podium (résultats) | SPF | `SPF010 3 POD 0447 F BELGA-0280` |
| **SPO** | ~3k | Sport (général, brèves) | BRF | `BRF014 3 SPO 0081 F BELGA-0280` |
| **MON** | ~2k | Mondial (Coupe du monde) | SPF | `SPF011 3 MON 0322 F BELGA-0172` |
| **TDF** | ~2k | Tour de France | SPF | `SPF016 3 TDF 0284 F BELGA-0302` |
| **CDM** | 382 | Coupe du Monde (variante) | SPF | `SPF005 3 CDM 0259 F BELGA-0065` |

> Note : `UIT` (Uitslagen, 173k) et `WED` (Wedstrijd, 3k) sont les équivalents
> NL de `RES` et des catégories de compétition.

### Communiqués et spéciaux

| Code | Volume (FR) | Signification | Préfixes typiques | Exemple |
|------|-------------|---------------|-------------------|---------|
| **EMC** | ~1,5k | Communiqués non rédactionnels | SDA, CMF, TTF | `SDA241 4 EMC 0183 F` |
| **FFF** | 83 | Communiqués UNS (fil commercial) | FPB | `FPB603 4 FFF 0355 F` |

> Note : `DDD` (NL) et `EEE` (EN) sont les équivalents de `FFF` pour les
> autres langues.

### Autres catégories (< 1000 occurrences)

| Code | Volume | Signification probable | Exemple |
|------|--------|----------------------|---------|
| **PRE** | ~500 | Presse (revue de presse) | `SPF036 3 PRE 0574 F BELGA-0306` |
| **EVE** | ~400 | Événements / agenda | `INT076 2 EVE 0527 B BELGA-0363` |
| **PRO** | ~270 | Programme (agenda sport) | `SPF008 3 PRO 1011 F BELGA-0096` |
| **RSB** | ~220 | Résultats sportifs belges (variante) | `SPF046 3 RSB 0501 B BELGA-0420` |
| **NAR** | 266 | Narration / éclairage | `SPF003 3 NAR 0059 F BELGA-0066` |
| **TAS** | 265 | ? | `SPF022 3 TAS 0322 F BELGA-0352` |
| **CLA** | 244 | Classements (variante de RAN) | `SPF012 3 CLA 0225 F BELGA-0091` |
| **SEL** | 157 | Sélections (sport) | `SPF012 3 SEL 0349 F BELGA-0083` |
| **BIL** | 150 | Bilingue (dépêches mixtes) | `SPF011 3 BIL 0433 F BELGA-0171` |

---

## 5. Codes langue

| Code | Signification | Notes | Exemple |
|------|---------------|-------|---------|
| **F** | Français | Grande majorité du fil | `... F BELGA-0001` |
| **B** | Bilingue | FR + NL dans le même texte, fréquent années 90–2000 | `... B BELGA-0340` |
| **T** | Tweetalig (alertes bilingues) | Toujours priorité 2, toujours ALERT dans le titre, à partir de 2010 | `... T BELGA-....` |
| **E** | English | Très rare (~22 occurrences), uniquement communiqués TTG/EMC | `TTG582 4 EMC 0182 E` |

Les dépêches `B` et `T` se retrouvent dans des fichiers `FKBR` comme `NKBR` — le nom de
fichier ne suffit pas à les identifier. Dans les `.FRA`, les bilingues (`B`) sont incluses.

---

## 6. Identifiant dépêche (champ optionnel IPTC 4.10)

| Format | Époque | Notes | Exemple |
|--------|--------|-------|---------|
| `BELGA-NNNN` | 1995–2002 (FRA) | Numéro séquentiel global du jour (4 chiffres) | `BELGA-0001`, `BELGA-2123` |
| `BELGA-....` | 2002–2019 (txt) | Placeholder — ID non attribué dans le fil texte | `BELGA-....` |
| `BELGA-NNNN` | 2002–2019 (txt, certaines) | ID réel quand disponible | `BELGA-0356` |

---

## 7. Suffixes (après l'identifiant)

| Suffixe | Signification | Exemple complet |
|---------|---------------|-----------------|
| *(vide)* | Dépêche standard | `INT136 3 GEN 0043 F BELGA-0666` |
| **COR NNN** | Correctif de la dépêche n°NNN | `INT001 3 GEN 0091 F BELGA-0031 COR 703` |
| **3 lettres** (initiales) | Journaliste auteur (BPE, DCM, TSA…) | `INT044 2 POL 0123 F BELGA-.... BPE` |
| **BELGASPORTS** | Provenance service sportif | `SPF074 3 RES 0141 F BELGA-0370 BELGASPORTS` |
| **NNN** (numérique) | Référence interne | `SPF225 3 GEN 0123 F BELGA-.... 154` |
| **PHOTO BELGA** | Photo disponible | `EXT004 3 POL 0265 F BELGA-0005 + PHOTO BELGA` |

---

## 8. Slugline (ligne 2)

Mots-clés en majuscules séparés par `/`. Hiérarchie thématique puis géographique.

| Type | Exemple |
|------|---------|
| Simple | `FOOTBALL/` |
| Multi-thème | `RUSSIE/GB/` |
| Géo + thème | `EU/ ENVIRONNEMENT/` |
| Complexe | `EUROPE/COMEURO/ENERGIE/AGENDA/` |
| Communiqué | `COMMUNIQUE/GVTFED/` |
| Avis de recherche | `DISPARITION/SGAP/` |
| Message de service | `ATTENTION USERS/BELGASERVICE/PRESS/` |

---

## 9. Titre (ligne 3)

Le titre peut contenir un indicateur de version en fin de ligne :

| Suffixe | Signification | Exemple |
|---------|---------------|---------|
| *(aucun)* | Première version | `Ligue des champions - résultats` |
| **(2)**, **(3)** | Mise à jour n°2, n°3 | `Ligue des champions - résultats (2)` |
| **(1LEAD)** | Premier lead / chapeau | `L'économie belge ralentit (1LEAD)` |
| **(3DER)** | Version finale (DER = dernier) | `Cht de Belgique (3DER): Van Herck en demi-finales` |
| **(CORRECT)** | Correction | `2465,8 millions de litres de lait (CORRECT)` |
| **(RECTIFICATIF)** | Correction (variante) | `Coupe de la Ligue - RECTIFICATIF -` |
| **(UPDATE)** | Mise à jour (variante) | `Résultats complets du championnat (UPDATE)` |
| **(PRESS)** | Conférence de presse / revue de presse | `Opel: le plan Magna prévoit la fermeture d'Opel Anvers (PRESS)` |

---

## 10. Dateline (ligne 4+)

Format : `   VILLE JJ/MM (SOURCE(S)) = début du texte`

### Sources principales

| Source | Type |
|--------|------|
| **BELGA** | Agence propre (dominante) |
| **AFP** | Agence France-Presse (2e source) |
| **DPA** | Deutsche Presse-Agentur |
| **ATS** | Agence Télégraphique Suisse |
| **BLOOMBERG** | Finance |

### Sources composites

Séparées par `-` ou `/` : `(AFP-BELGA)`, `(AFP/DPA)`, `(DPA/AFP/BELGA)`, etc.

### Exemple

```
   BRUXELLES 23/07 (AFP-DPA-REUTER) = Dernier résultat des matches...
```

> Note : `ANP` (Algemeen Nederlands Persbureau) apparaît principalement sur
> le fil néerlandophone.

---

## 11. Marqueur de fin

### Format

`./.` suivi optionnellement des initiales du journaliste.

| Forme | Signification | Exemple |
|-------|---------------|---------|
| `./.` | Fin simple | `./.` |
| `./.XXX` | Fin + initiales auteur | `./.CVN`, `./.LME`, `./.DCM` |
| `././.XXX` | Variante (double séparateur) | `././.MIK` |
| `./. XXX` | Avec espace | `./. CER` |

### Initiales en fin de corps (alternative)

Parfois les initiales apparaissent sur la dernière ligne du corps :

```
VDH/FUL/                  ← auteur/éditeur de desk
ALB/MIK/                  ← auteur/relecteur
```

---

## 12. DTG — Date-Time Group (IPTC 6.2)

Format : `JJHHMM MOIS AA`

| Composant | Format | Exemple |
|-----------|--------|---------|
| Jour | 2 chiffres | `31` |
| Heure + minute | 4 chiffres (HHMM) | `0001` |
| Mois | 3 lettres anglaises | `JUL` |
| Année | 2 chiffres | `97` |

Mois possibles : `JAN`, `FEB`, `MAR`, `APR`, `MAY`, `JUN`, `JUL`, `AUG`, `SEP`, `OCT`, `NOV`, `DEC`.

Exemple complet : `310001 JUL 97` → 31 juillet 1997 à 00h01.

---

## 13. Horodatage XML — ISO 8601 basique

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

| Balise | Rôle | Exemple |
|--------|------|---------|
| `FirstCreated` | Date de première rédaction | `20220211T044456` |
| `ThisRevisionCreated` | Date de la révision courante | `20220211T045731` |
| `DateAndTime` (NewsEnvelope) | Date de publication/distribution | `20250315T144554` |
| `DateId` | Identifiant temporel (= FirstCreated en général) | `20220211T044456` |
| `ValidationDate` | Date de validation éditoriale | `20250731T155612` |

---

## 14. Horodatage session télex (optionnel)

Présent uniquement dans les fichiers `.FRA`. Marque le moment de réception sur le terminal télex.

Format : `[JJ-MOIS-AA  HH:MM]`

Exemple : `[31-JUL-97  00:00]`

---

## 15. Séparateur de dépêches (fichiers .FRA)

Les dépêches sont séparées par la séquence :

```
./.
JJHHMM MOIS AA
```

Chaque fichier quotidien contient ~250 dépêches.

---

## 16. Noms de fichiers

| Extension | Format | Époque | Exemple |
|-----------|--------|--------|---------|
| `.FRA` | `JJMMAA.FRA` ou `JJMMAAA.FRA` | 1995–2002 | `310797.FRA`, `08042002.FRA` |
| `.txt` | `FKBR[datetime]_[id].txt` | 2002–2019 | `FKBR200706150920_141.txt` |
| `.xml` | `FKBR[datetime]_[id].xml` | 1994–2026 | `FKBR199406150000_10020940.xml` |

Préfixe `F` = français. `KBR` = identifiant archive (Koninklijke Bibliotheek).

> Les dépêches bilingues (`B`, `T`) peuvent se trouver dans des fichiers `FKBR`
> ou `NKBR` indifféremment. Dans les `.FRA`, les bilingues sont incluses.

---

## 17. Métadonnées propres au XML

Champs présents uniquement dans les fichiers `.xml`, sans équivalent dans le format texte.

### Genre

| Valeur | Époque | Signification |
|--------|--------|---------------|
| `""` (vide) | Toutes | Valeur par défaut (majorité des dépêches) |
| `"1"` | 1994–~2010 | Format classique — probablement « actualité courante » |
| `"CURRENT"` | ~2019+ | Format moderne — même signification que `"1"` |

Exemple : `<Genre FormalName="CURRENT"/>`

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

| Valeur | Volume | Signification probable | Exemple |
|--------|--------|----------------------|---------|
| `S1` | majoritaire | Section 1 (actualité principale ?) | `<Property FormalName="Label" Value="S1"/>` |
| `S3` | rare | Section 3 | `<Property FormalName="Label" Value="S3"/>` |
| `F1` | rare | ? | `<Property FormalName="Label" Value="F1"/>` |
| `R2` | rare | ? | `<Property FormalName="Label" Value="R2"/>` |

### Distribution

Toujours `Default` (~99,9%). Une seule occurrence de `B` dans tout le corpus.

### Update (attribut de `RevisionId`)

Toujours `"N"`. Les mises à jour sont identifiées par le numéro
de `RevisionId` (1, 2, 3…).

Exemple : `<RevisionId PreviousRevision="0" Update="N">4</RevisionId>`

### Balises toujours vides

Présentes dans les XML modernes (~2019+) mais systématiquement vides :

| Balise | Contexte | Exemple |
|--------|----------|---------|
| `Contributor/Party` | `AdministrativeMetadata` | `<Party FormalName=""/>` |
| `SubjectCode` | `DescriptiveMetadata` | `<SubjectCode/>` |
| `Property SubLocation` | `Location` | `<Property FormalName="SubLocation"/>` |
| `NewsService` (dans `NewsEnvelope`) | Doublon de `NewsPackage`, toujours vide | `<NewsService FormalName=""/>` |
| `NewsProduct` (dans `NewsEnvelope`) | Doublon de `NewsPackage`, toujours vide | `<NewsProduct FormalName=""/>` |
