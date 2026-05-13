# Métacommunication Belga — typologie et chronologie

*Analyse réalisée le 2026-05-04 à partir de `donnees/bdd/depeches.duckdb` (table `depeches`, 6,3 M dépêches 1994-2026).*

## 1. Définition et périmètre

On appelle ici « métacommunication » toute dépêche diffusée sur le fil Belga dont le contenu **ne relève pas du rédactionnel d'actualité**, mais d'une fonction interne :
- annonces de programmation et planning rédactionnel,
- veille média (revues de presse, sommaires JT),
- communiqués officiels relayés (Palais, Moniteur, prix carburants),
- récapitulatifs et bilans périodiques,
- corrections, kills, advisories.

Volume identifiable par patterns de headline : **~265 000 dépêches, ≈ 4,2 % du corpus**.

## 2. Vue d'ensemble par produit

Décompte sur l'ensemble du corpus, headlines détectables :

| Produit | Volume | Mots moy. | Période |
|---|---:|---:|---|
| BelgaService (méta-format, voir §4) | 103 616 | 359 | 2006-2023 |
| BELGA NEXT | 51 671 | 218 | 1999-2003 |
| ATTENTION USERS / ATTENTION ALL USERS | 41 615 | 384 | 1999-2019 |
| BELGANIGHT | 40 874 | 208 | 2002-2010 |
| PROGRAM OF THE DAY | 9 996 | **3 409** | 2002-2021 |
| CORRECTION / CORRECTIE | 7 774 | 255 | 1994-2026 |
| JOUR DD/MM (agenda du jour, sans préfixe) | 6 035 | **3 122** | 2014-2023 |
| RECAP / BILAN / JAAROVERZICHT | 3 578 | 592 | 1994-2026 |
| AGENDA | 1 324 | 185 | 1994-2023 |
| ADVISORY / AVIS | 798 | 199 | 1994-2025 |
| KILL / TUER | 619 | 270 | 1994-2025 |

**Lecture** : ce ne sont pas des produits parallèles, mais une **succession de formats** qui se relaient — chaque produit a sa fenêtre temporelle (cf. §3).

## 3. Quatre ères chronologiques

| Ère | Période | Caractère | Produits dominants |
|---|---|---|---|
| **1. Silencieuse** | 1994-1998 | métacomm absente (ou non archivée) du fil | qq ATTENTION USERS isolés |
| **2. Formats courts** | 1999-2009 | annonces brèves type télex, ~200 mots | BELGA NEXT, BELGANIGHT, ATTENTION USERS |
| **3. Formats longs** | 2010-2023 | bulletins consolidés, ~3 000 mots | BelgaService, PROGRAM OF THE DAY, JOUR DD/MM |
| **4. Silencieuse à nouveau** | 2024-2026 | extinction sur le fil principal | aucun produit systématique détectable |

Détail année par année (volumes par produit) :

| Année | ATTENTION | BELGA NEXT | BELGANIGHT | BelgaService | PROGRAM | JOUR DD/MM |
|---:|---:|---:|---:|---:|---:|---:|
| 1999 | 2 130 | 6 602 | – | – | – | – |
| 2000 | 5 386 | 14 431 | – | – | – | – |
| 2001 | 6 415 | 16 505 | – | – | – | – |
| 2002 | 4 421 | 14 120 | 5 135 | – | 3 | – |
| 2003 | 4 456 | 8 | 5 917 | – | – | – |
| 2004 | 4 092 | – | 5 773 | – | 1 | – |
| 2005 | 4 087 | – | 5 291 | – | – | – |
| 2006 | 2 324 | – | 3 170 | 184 | – | – |
| 2007 | 2 815 | – | 5 211 | 4 454 | 6 | – |
| 2008 | 2 686 | – | 4 863 | 10 856 | – | – |
| 2009 | 2 118 | – | 5 014 | 10 207 | 14 | – |
| 2010 | 766 | – | 500 | 9 906 | 453 | – |
| 2011 | 3 | – | – | 2 035 | 223 | – |
| 2012 | 4 | – | – | 9 840 | 1 269 | – |
| 2013 | – | – | – | 9 958 | 1 290 | – |
| 2014 | – | – | – | 9 492 | 1 272 | 30 |
| 2015 | 4 | – | – | 9 458 | 1 343 | – |
| 2016 | 1 | – | – | 8 549 | 1 272 | – |
| 2017 | 2 | – | – | 8 253 | 1 249 | 4 |
| 2018 | 8 | – | – | 8 417 | 1 268 | 32 |
| 2019 | 15 | – | – | 2 001 | 303 | 1 075 |
| 2020 | 1 | – | – | 3 | 14 | 1 307 |
| 2021 | – | – | – | 2 | 16 | 1 348 |
| 2022 | – | – | – | – | – | 1 417 |
| 2023 | 1 | – | – | 1 | – | 822 |
| 2024+ | – | – | – | – | – | – |

**Pivots éditoriaux clairs**

- **2010** : BELGANIGHT meurt (5 014 → 500), ATTENTION USERS chute (2 118 → 766), PROGRAM OF THE DAY explose (14 → 453). Premier basculement majeur.
- **2019-2020** : BelgaService meurt (8 417 → 2 001 → 3), PROGRAM s'efface (1 268 → 303 → 14), JOUR DD/MM prend le relais (32 → 1 075 → 1 307). Cohérent avec la rupture format documentée par ailleurs (`project_depeche_rupture_format_2020`).
- **2023-2024** : extinction totale sur le fil principal. Recherches sur tous les patterns plausibles (agenda, preview, program, au menu, à venir, semaine du, week, overzicht, recap, headlines tout-majuscules, headlines récurrentes ≥30 occ.) : **aucun nouveau format systématique détecté**. La métacommunication a probablement migré hors XML (dashboard interne, autre canal).

## 4. BelgaService comme méta-format

Le préfixe `BelgaService` (séparateur `-` ou `:`, cf. `feedback_headlines_belgaservice`) regroupe **~10 sous-produits distincts** :

| Famille | Volume | Mots moy. | Période |
|---|---:|---:|---|
| **Mediawatch** (revue audiovisuel) | 56 854 (55 %) | 288 | 2007-2019 |
| **Titres presse écrite** (journaux / krantentitels) | 13 614 | 423 | 2006-2019 |
| Autre (à recatégoriser, voir §4.2) | 9 037 | 449 | 2006-2023 |
| **Sommaires JT** (hoofdpunten journaal) | 6 970 | 427 | 2006-2019 |
| **Communiqués Palais / officiels** | 6 190 | 68 | 2006-2018 |
| **Planning / Program** | 6 021 | 381 | 2007-2019 |
| **Prix carburants** (max prix petroleum.) | 2 806 | 120 | 2006-2020 |
| Moniteur belge | 888 | 591 | 2006-2012 |
| **Récap mensuel/annuel** (Maandoverzicht, etc.) | 694 | **4 901** | 2007-2019 |
| **Bilan sportif mensuel** | 112 | **8 070** | 2008-2019 |

### 4.1 Constats marquants

- **75 % de BelgaService = veille média** (Mediawatch + Titres presse + Sommaires JT = 77 438 dépêches). Confirme `project_pics_horaires_depeches` : Mediawatch est un service automatisé, déclinable par chaîne (RTL, RTBF, AVS, JT), par jour, par émission.
- **Bilan sportif mensuel : 112 dépêches mais 8 070 mots de moyenne** → ces bulletins sont à l'origine des records de longueur du corpus (jusqu'à **19 928 mots** en 2015). Concentré 2015-2016. Très rares mais visuellement très lourds sur la heatmap `mots_par_depeche`.
- **Communiqués Palais ultra-courts (68 mots)** — agenda royal du jour, format télex pur.
- **Tous éteints en 2019-2020** sauf Prix carburants (jusqu'en 2020) et la queue résiduelle "autre" jusqu'en 2023.

### 4.2 Sous-familles dans le bloc « autre » (9 037 dépêches)

Identifiées par premier mot après séparateur, à intégrer dans une 2e itération de classification :
- Calendrier sportif international / internationale sportkalender (~670)
- Audiences / activités royales / audiënties ten paleize (~615) → à fusionner avec Communiqués Palais
- Sommaires d'émissions TV (Terzake, Knack, Rob Vandaag, Villa Politica) (~660)
- Persmededeling van het… (~110) → à fusionner avec Communiqués
- Belga planning update / update Belga (~684) → à fusionner avec Planning
- Sportjaaroverzicht (~150) → à fusionner avec Bilan sportif
- CIM / audiences TV (~150)
- Bulletin pollens « rhume des foins » (~130)

## 5. Implications pour les analyses

### 5.1 Heatmap `mots_par_depeche` (graphique d'origine)

La queue >800 mots (56 276 dépêches, 0,9 % du corpus) est **massivement non-rédactionnelle** :
- ~45 % = programmes/agendas (PROGRAM OF THE DAY, JOUR DD/MM, ATTENTION USERS)
- ~10 % = bilans BelgaService et récaps mensuels (responsables des records >10 000 mots, concentrés 2015-2016)
- Le reste = vraies longues dépêches éditoriales (plafonnaient ~1 500 mots avant 2007)

Les ruptures visibles sur la heatmap (2010-2011, 2019-2020) sont des **artefacts d'apparition/extinction de produits métacommunicationnels**, pas des changements de pratique rédactionnelle.

### 5.2 Filtre proposé pour étudier la longueur rédactionnelle réelle

Exclure :
- `service ∈ {BIN, INT}` ET `headline` matchant `^(PROGRAM|ATTENTION|MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY|SUNDAY|BelgaService|BELGA NEXT|BELGANIGHT)`
- les `CORRECTION`, `KILL`, `ADVISORY` (transverses, ~9 200 dépêches au total)

### 5.3 Comparaisons longitudinales

- 2024-2026 = corpus « plus pur » que jamais (pas de métacomm sur le fil).
- 2010-2023 = à filtrer rigoureusement pour comparaison équitable avec 2024+.
- 1994-1998 = également « pur » mais pour une raison différente (métacomm pas encore instaurée).

## 6. Pistes ouvertes

1. **Streamgraph dédié** des produits métacommunicationnels par année — visualisation des relais successifs et des deux pivots 2010 et 2019.
2. **Recatégorisation fine du bloc « autre »** de BelgaService (§4.2).
3. **Vérification 2024-2026** : confirmer auprès de Belga (ou via fichiers source) que la métacomm a bien migré hors XML, et où.
4. **Cross-check Mediawatch ↔ pics horaires 13h30/19h40** : vérifier que l'extinction de Mediawatch en 2019 coïncide avec la disparition des pics documentés.

## Annexe — patterns SQL utilisés

Détection des produits principaux sur le champ `headline` :

```sql
CASE
  WHEN headline ILIKE 'PROGRAM OF THE DAY%' THEN 'PROGRAM OF THE DAY'
  WHEN headline ILIKE 'ATTENTION USERS%' OR headline ILIKE 'ATTENTION ALL USERS%' THEN 'ATTENTION USERS'
  WHEN headline ILIKE 'BELGANIGHT%' OR headline ILIKE 'BELGA NIGHT%' THEN 'BELGANIGHT'
  WHEN headline ILIKE 'BELGA NEXT%' THEN 'BELGA NEXT'
  WHEN headline ILIKE 'BelgaService%' THEN 'BelgaService'
  WHEN regexp_matches(headline, '^(MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY|SUNDAY) [0-9]') THEN 'JOUR DD/MM (agenda)'
  WHEN headline ILIKE 'AGENDA%' THEN 'AGENDA'
  WHEN headline ILIKE 'JAAROVERZICHT%' OR headline ILIKE 'RETROSPECTIVE%' OR headline ILIKE 'BILAN%' THEN 'RECAP/BILAN'
  WHEN headline ILIKE 'CORRECTION%' OR headline ILIKE 'CORRECTIE%' THEN 'CORRECTION'
  WHEN headline ILIKE 'KILL%' OR headline ILIKE 'TUER%' THEN 'KILL'
  WHEN headline ILIKE 'ADVISORY%' OR headline ILIKE 'AVIS%' THEN 'ADVISORY'
END
```

Sous-typage BelgaService — extraction du suffixe puis classement sur premier mot/expression :

```sql
regexp_extract(headline, 'BelgaService\s*[:\-]\s*(.+)', 1) AS suffixe
```
