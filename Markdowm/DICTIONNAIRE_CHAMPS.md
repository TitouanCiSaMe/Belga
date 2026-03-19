# Dictionnaire des champs — Dépêches BELGA

Référence exhaustive de toutes les valeurs observées dans le corpus (3,8M de dépêches, 1994–2026).

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

### Principaux (> 10 000 occurrences)

| Préfixe | Volume | Langue | Signification | Exemple |
|---------|--------|--------|---------------|---------|
| **BIN** | 792k | N (98%) | Binnenland — actualité intérieure néerlandophone | `BIN022 3 ALG 0123 N BELGA-....` |
| **INT** | 709k | F (95%) | Intérieur — actualité intérieure francophone | `INT136 3 GEN 0043 F BELGA-0666` |
| **SPF** | 665k | F (80%) + B (14%) | Sport/Presse Francophone | `SPF001 3 RES 0070 F BELGA-0001` |
| **EXT** | 618k | F (98%) | Extérieur — international francophone | `EXT059 3 POL 0304 F BELGA-0356` |
| **SPN** | 597k | N (76%) + B (16%) | Sport/Presse Néerlandophone | `SPN184 3 UIT 0178 N BELGA-2123` |
| **BTL** | 436k | N (99%) | Buitenland — international néerlandophone | `BTL003 3 ECO 0079 N BELGA-0058` |
| **BRN** | 12k | N | Brèves néerlandophones | `BRN001 3 ALG 0123 N BELGA-....` |
| **BRF** | 11k | F | Brèves francophones | `BRF001 3 GEN 0123 F BELGA-....` |

### Secondaires (100–2000 occurrences)

| Préfixe | Volume | Langue | Signification | Exemple |
|---------|--------|--------|---------------|---------|
| **TTG** | 1 587 | N / E | Communiqués tweetalig/anglais (économie, entreprises) | `TTG582 4 EMC 0182 E` |
| **TTF** | 118 | F | Communiqués francophones (même famille que TTG) | `TTF312 4 EMC 0690 F` |
| **TTB** | 26 | B | Communiqués bilingues (même famille) | `TTB579 4 EMC 0903 F  INTL GALILEO FRENCH` |
| **TTE** | 97 | — | Communiqués (même famille, variante) | `TTE282 4 EMC 0446 F` |
| **VLR** | 586 | N | Vlaamse Regering — communiqués du gouvernement flamand | `VLR146 3 EMC 0240 N` |
| **VLM** | 161 | N | Vlaamse Mededeling — même type que VLR | `VLM005 3 EMC 0603 N` |
| **DVO** | 207 | N | Dienst Voorlichting Opsporingen — avis de recherche NL | `DVO236 4 EMC 0172 N` |
| **SDA** | 205 | F | Service Diffusion Avis — avis de recherche FR (SGAP/police) | `SDA241 4 EMC 0183 F` |
| **VKA–VKI** | ~500 total | N | Séries de communiqués NL (VKA, VKB, VKC… VKI) | `VKA001 3 EMC 0144 N` |
| **FPB** | 83 | F | Fil Presse Belgique — communiqués UNS (Universal News Services) FR | `FPB603 4 FFF 0355 F` |
| **NPB** | 100 | N | Nieuws Pers België — même chose en NL | `NPB604 4 DDD 0365 N` |

### Rares (< 100 occurrences)

| Préfixe | Volume | Signification | Exemple |
|---------|--------|---------------|---------|
| **CMN** | 42 | Communiqués/Mededelingen NL | `CMN001 3 EMC 0146 N BELGA-0280` |
| **CMF** | 35 | Communiqués non rédactionnels FR | `CMF001 3 EMC 0130 F BELGA-0046 C` |
| **CMQ** | 4 | Communiqués (variante) | `CMQ001 4 EMC 0063 F` |
| **IBIN** | 4 | Binnenland (variante interne ?) | `IBIN008 3 FIN 0230 N BELGA-....` |
| **BINT** | 1 | Buitenland-Intérieur (hybride ?) | `BINT007 3 GEN 0351 F BELGA-....` |
| **SPC** | 2 | Sport Compétition (?) | `SPC002 3 UIT 0103 N BELGA-0338` |
| **BFR** | 2 | Brèves France (?) | `BFR015 2 GEN 0192 F BELGA-....` |

---

## 3. Priorités

| Code | Niveau | Volume | Usage | Exemple |
|------|--------|--------|-------|---------|
| **1** | Flash | 211 | Événement exceptionnel (mort chef d'État, attentat majeur) | `INT001 1 POL 0025 F BELGA-....` |
| **2** | Urgent / Alert | 140k | Breaking news | `INT044 2 POL 0123 F BELGA-.... BPE` |
| **3** | Normal | 3,7M | Standard — 96% du corpus | `EXT059 3 POL 0304 F BELGA-0356` |
| **4** | Différé | 1 337 | Background, features, communiqués de presse | `TTG582 4 EMC 0182 E` |

---

## 4. Catégories (rubriques)

### Actualité générale

| Code | Volume | Signification | Langue | Préfixes typiques | Exemple |
|------|--------|---------------|--------|-------------------|---------|
| **GEN** | 1,16M | Général | FR | INT, EXT, SPF | `INT136 3 GEN 0043 F BELGA-0666` |
| **ALG** | 1,03M | Algemeen (général) | NL | BIN, BTL, SPN | `BIN022 3 ALG 0123 N BELGA-....` |
| **POL** | 588k | Politique | FR + NL | INT, EXT, BIN, BTL | `EXT059 3 POL 0304 F BELGA-0356` |
| **ECO** | 427k | Économie | FR + NL | INT, EXT, BIN, BTL | `BTL003 3 ECO 0079 N BELGA-0058` |
| **FIN** | 36k | Finance / marchés | FR + NL | BIN, INT | `EXT002 3 FIN 0284 F BELGA-0003` |
| **PRV** | 35k | Provinciale (régional) | FR + NL | BIN, INT | `INT082 2 PRV 0638 B BELGA-0401` |
| **EUR** | 26k | Europe | NL | BTL | `BRN012 2 EUR 0146 N BELGA-0311` |
| **CLT** | 6k | Culture | FR + NL | EXT, BTL | `EXT051 2 CLT 0485 F BELGA-0266` |

### Sport

| Code | Volume | Signification | Langue | Préfixes typiques | Exemple |
|------|--------|---------------|--------|-------------------|---------|
| **UIT** | 173k | Uitslagen (résultats sportifs) | NL | SPN | `SPN184 3 UIT 0178 N BELGA-2123` |
| **RES** | 139k | Résultats sportifs | FR | SPF | `SPF001 3 RES 0070 F BELGA-0001` |
| **REB** | 79k | Résultats sportifs belges | FR + NL | SPF, SPN | `SPF044 3 REB 0088 B BELGA-0209` |
| **RAN** | 61k | Rankings / classements | FR + NL | SPF, SPN | `SPF017 3 RAN 0152 B BELGA-0107` |
| **SPO** | 6k | Sport (général, brèves) | FR + NL | BRF, BRN | `BRN014 3 SPO 0081 N BELGA-0280` |
| **OLY** | 20k | Jeux Olympiques | FR + NL | SPF, SPN | `SPF017 3 OLY 0509 F BELGA-0318` |
| **HIP** | 12k | Hippisme (général) | FR + NL | SPF, SPN | `SPF059 3 HIP 0128 F BELGA-0580 TFX` |
| **HFR** | 5k | Hippisme France (résultats courses françaises) | FR | SPF | `SPF057 3 HFR 0123 F BELGA-....` |
| **POD** | 8k | Podium (résultats sportifs) | FR + NL | SPF, SPN | `SPF010 3 POD 0447 F BELGA-0280` |
| **MON** | 4k | Mondial (Coupe du monde) | FR + NL | SPF, SPN | `SPF011 3 MON 0322 F BELGA-0172` |
| **TDF** | 4k | Tour de France | FR + NL | SPF, SPN | `SPF016 3 TDF 0284 F BELGA-0302` |
| **WED** | 3k | Wedstrijd (compétition) | NL | SPN | `SPN001 3 WED 0244 N BELGA-0050` |
| **CDM** | 382 | Coupe du Monde (variante) | FR | SPF | `SPF005 3 CDM 0259 F BELGA-0065` |

### Communiqués et spéciaux

| Code | Volume | Signification | Langue | Préfixes typiques | Exemple |
|------|--------|---------------|--------|-------------------|---------|
| **EMC** | 3 579 | Communiqués non rédactionnels | FR + NL | VLR, DVO, SDA, TTG, CMN, CMF | `VLR146 3 EMC 0240 N` |
| **FFF** | 83 | Communiqués UNS (fil commercial FR) | FR | FPB | `FPB603 4 FFF 0355 F` |
| **DDD** | 83 | Communiqués UNS (fil commercial NL) | NL | NPB | `NPB604 4 DDD 0365 N` |
| **EEE** | 17 | Communiqués UNS (fil commercial EN) | EN | NPB | `NPB613 4 EEE 0350 N` |

### Autres catégories (< 1000 occurrences)

| Code | Volume | Signification probable | Exemple |
|------|--------|----------------------|---------|
| **PRE** | 1 070 | Presse (revue de presse ?) | `SPF036 3 PRE 0574 F BELGA-0306` |
| **EVE** | 778 | Événements / agenda | `INT076 2 EVE 0527 B BELGA-0363` |
| **PRO** | 534 | Programme (agenda sport ?) | `SPF008 3 PRO 1011 F BELGA-0096` |
| **RSB** | 447 | Résultats sportifs belges (variante) | `SPF046 3 RSB 0501 B BELGA-0420` |
| **NAR** | 266 | Narration / éclairage ? | `SPF003 3 NAR 0059 F BELGA-0066` |
| **TAS** | 265 | ? | `SPF022 3 TAS 0322 F BELGA-0352` |
| **SOC** | 249 | Social / société | `BRN010 3 SOC 0088 N BELGA-0206` |
| **CLA** | 244 | Classements (variante de RAN) | `SPF012 3 CLA 0225 F BELGA-0091` |
| **SEL** | 157 | Sélections (sport) | `SPF012 3 SEL 0349 F BELGA-0083` |
| **BIL** | 150 | Bilingue (dépêches mixtes) | `SPF011 3 BIL 0433 F BELGA-0171` |
| **MED** | 127 | Médias | `SPN003 3 MED 0043 N BELGA-0052` |

---

## 5. Codes langue

| Code | Langue | Volume | Notes | Exemple |
|------|--------|--------|-------|---------|
| **F** | Français | 1,96M | — | `... F BELGA-0001` |
| **N** | Néerlandais | 1,80M | — | `... N BELGA-0058` |
| **B** | Bilingue | 48k | FR + NL dans le même texte, fréquent années 90–2000 | `... B BELGA-0340` |
| **T** | Tweetalig (alertes bilingues) | 36k | Toujours priorité 2, toujours ALERT dans le titre, à partir de 2010 | `... T BELGA-....` |
| **E** | English | ~22 | Très rare, uniquement communiqués TTG/EMC | `TTG582 4 EMC 0182 E` |

---

## 6. Identifiant dépêche (champ optionnel IPTC 4.10)

| Format | Époque | Notes | Exemple |
|--------|--------|-------|---------|
| `BELGA-NNNN` | 1995–2002 (FRA/NED) | Numéro séquentiel global du jour (4 chiffres) | `BELGA-0001`, `BELGA-2123` |
| `BELGA-....` | 2002–2019 (txt) | Placeholder — ID non attribué dans le fil texte | `BELGA-....` |
| `BELGA-NNNN` | 2002–2019 (txt, certaines) | ID réel quand disponible | `BELGA-0356` |

---

## 7. Suffixes (après l'identifiant)

| Suffixe | Signification | Exemple complet |
|---------|---------------|-----------------|
| *(vide)* | Dépêche standard | `INT136 3 GEN 0043 F BELGA-0666` |
| **COR NNN** | Correctif de la dépêche n°NNN | `BIN216 3 ALG 0123 N BELGA-.... COR 908` |
| **3 lettres** (initiales) | Journaliste auteur (AVM, FEM, TSA…) | `BIN001 3 POL 0432 N BELGA-0004 AVM` |
| **BELGASPORTS** | Provenance service sportif | `SPF074 3 RES 0141 F BELGA-0370 BELGASPORTS` |
| **DCM** | Initiales desk | `SPF225 3 GEN 0123 F BELGA-.... DCM` |
| **BPE** | Initiales journaliste | `INT044 2 POL 0123 F BELGA-.... BPE` |
| **NNN** (numérique) | Référence interne | `SPF225 3 GEN 0123 F BELGA-.... 154` |
| **NEXT** | Suite (dépêche sur plusieurs messages ?) | `BTL003 3 POL 0162 N BELGA-0010 NEXT` |
| **PHOTO BELGA** | Photo disponible | `EXT004 3 POL 0265 F BELGA-0005 + PHOTO BELGA` |

---

## 8. Slugline (ligne 2)

Mots-clés en majuscules séparés par `/`. Hiérarchie thématique puis géographique.

| Type | Exemple |
|------|---------|
| Simple | `FOOTBALL/` |
| Multi-thème | `RUSSIE/GB/` |
| Géo + thème | `EU/ ENVIRONNEMENT/` |
| Bilingue | `KOERSEN/ COURS/ BEURS/ BOURSE/` |
| Complexe | `BEDRIJVEN/ZWITSERLAND/VS/GERECHT/AGENDA/` |
| Communiqué | `PERSMEDEDELING/VLAREG/ALG/RAMPEN/` |
| Alert | `WIELRENNEN/TOUR DE FRANCE/ALERT/` |
| Avis de recherche | `OPSPORINGSBERICHTEN/APSD/` |

---

## 9. Titre (ligne 3)

Le titre peut contenir un indicateur de version en fin de ligne :

| Suffixe | Signification | Exemple |
|---------|---------------|---------|
| *(aucun)* | Première version | `Ligue des champions - résultats` |
| **(2)**, **(3)** | Mise à jour n°2, n°3 | `Ligue des champions - résultats (2)` |
| **(1LEAD)** | Premier lead / chapeau | `Krimp Belgische economie vertraagt (NBB) (1LEAD)` |
| **(3DER)** | Version finale (DER = dernier) | `Cht de Belgique (3DER): Van Herck en demi-finales` |
| **(CORRECT)** | Correction | `2465,8 miljoen (CORRECT) liter melk` |
| **(RECTIFICATIF)** | Correction (variante bilingue) | `Coupe de la League - Ligabeker - VERBETERING/RECTIFICATIF -` |
| **(UPDATE)** | Mise à jour (variante) | `Zes Nederlanders dood bij busongeluk Spanje (UPDATE)` |
| **(PRESS)** | Conférence de presse / revue de presse | `Opel: businessplan Magna voorziet sluiting Opel Antwerpen in 2010 (PRESS)` |

---

## 10. Dateline (ligne 4+)

Format : `   VILLE JJ/MM (SOURCE(S)) = début du texte`

### Sources principales

| Source | Volume | Type |
|--------|--------|------|
| **BELGA** | dominante | Agence propre |
| **AFP** | 2e source | Agence France-Presse |
| **DPA** | 3e source | Deutsche Presse-Agentur |
| **ANP** | 4e source | Algemeen Nederlands Persbureau |
| **ATS** | rare | Agence Télégraphique Suisse |
| **BLOOMBERG** | rare | Finance |
| **TNL** | rare | ? |

### Sources composites

Séparées par `-` ou `/` : `(AFP-BELGA)`, `(AFP/DPA)`, `(DPA/AFP/BELGA)`, `(ANP-BELGA)`, etc.

### Exemple

```
   BRUXELLES 23/07 (AFP-DPA-REUTER) = Dernier résultat des matches...
```

---

## 11. Marqueur de fin

### Format

`./.[INITIALES]` — le `./.` termine la dépêche, suivi optionnellement des initiales du journaliste.

| Forme | Signification | Exemple |
|-------|---------------|---------|
| `./.` | Fin simple | `./.` |
| `./.XXX` | Fin + initiales auteur | `./.CVN`, `./.MIK`, `./.DCM` |
| `././.XXX` | Variante (double séparateur) | `././.MIK`, `././.RKO` |
| `./. XXX` | Avec espace | `./. CER` |

### Initiales en fin de corps (alternative)

Parfois les initiales apparaissent sur la dernière ligne du corps au lieu du marqueur `./.` :

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

| Balise | Rôle | Exemple |
|--------|------|---------|
| `FirstCreated` | Date de première rédaction | `20220211T044456` |
| `ThisRevisionCreated` | Date de la révision courante | `20220211T045731` |
| `DateAndTime` (NewsEnvelope) | Date de publication/distribution | `20250315T144554` |
| `DateId` | Identifiant temporel (= FirstCreated en général) | `20220211T044456` |
| `ValidationDate` | Date de validation éditoriale | `20250731T155612` |

Le `T` est le séparateur standard ISO 8601 entre date et heure.
C'est l'équivalent numérique du DTG texte (`310001 JUL 97`).

---

## 15. Horodatage session télex (optionnel)

Présent uniquement dans les fichiers `.FRA`/`.NED`. Marque le moment de réception sur le terminal télex.

Format : `[JJ-MOIS-AA  HH:MM]`

Exemple : `[31-JUL-97  00:00]`

---

## 16. Séparateur de dépêches (fichiers .FRA/.NED)

Les dépêches sont séparées par la séquence :

```
./.
JJHHMM MOIS AA
```

Chaque fichier quotidien contient ~250 dépêches.

---

## 17. Noms de fichiers

| Extension | Format | Époque | Exemple |
|-----------|--------|--------|---------|
| `.FRA` | `JJMMAA.FRA` ou `JJMMAAA.FRA` | 1995–2002 | `310797.FRA`, `08042002.FRA` |
| `.NED` | `JJMMAA.NED` ou `JJMMAAA.NED` | 1995–2002 | `310797.NED` |
| `.txt` | `XKBR[datetime]_[id].txt` | 2002–2019 | `FKBR200706150920_141.txt` |
| `.xml` | `XKBR[datetime]_[id].xml` | 1994–2026 | `FKBR199406150000_10020940.xml` |

Préfixe nom de fichier : `F` = français, `N` = néerlandais. `KBR` = identifiant archive (Koninklijke Bibliotheek).

---

## 18. Métadonnées propres au XML

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

| Valeur | Volume | Notes | Exemple |
|--------|--------|-------|---------|
| `Default` | ~99,9% | Distribution standard | `<Property FormalName="Distribution" Value="Default"/>` |
| `B` | 1 occurrence | Distribution restreinte ? | `<Property FormalName="Distribution" Value="B"/>` |

### Update (attribut de `RevisionId`)

Toujours `"N"` dans le corpus BELGA. La spec NewsML prévoit aussi `"U"` (update),
mais BELGA ne l'utilise pas — les mises à jour sont identifiées par le numéro
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
