# Évolution de la longueur des dépêches BELGA (1995-2025)

Analyse de `heatmap_mots_annees_comparaison.png`
(`code/depeches/graphiques/mots_par_depeche.py`).
Session du 2026-05-13.

## 1. Lecture du graphique

Heatmap : une ligne par année, l'axe X = nombre de mots par dépêche
(0 à 800, queue ≥790 cumulée dans la dernière tranche). Chaque ligne
est normalisée → la couleur représente la **part relative** des
dépêches de l'année dans chaque tranche de 10 mots. La courbe rose
superpose la médiane annuelle.

Deux panneaux : avant filtrage / après exclusion de la
métacommunication (cascade `EXPR_METACOMM`). L'effet du filtrage sur
les modes principaux est **quasi nul** (cf. §4).

## 2. Trois régimes de format

Les fortes taches claires correspondent au **mode** (pic de densité)
du nombre de mots par dépêche chaque année. Trois régimes successifs :

| Régime | Période | Pic modal | Année la plus marquée |
|---|---|---|---|
| 1 | 1995 – ~2009 | **130-140 mots** | 2000 (6,2 % de l'année) |
| 2 | 2010 – 2013 | **240-250 mots** | 2011 (5,9 %) |
| 3 | 2014 – 2025 | **290-300 mots** | 2025 (6,8 %) |

Le format modal d'une dépêche BELGA a **roughly doublé** sur la
période. Les transitions 2010 et 2014 sont des **ruptures de format**,
pas des dérives progressives.

## 3. Effet de sujet ou moyenne globale ?

Pour chaque pic modal, distribution des services et catégories dans
la cellule modale comparée à la part globale de l'année :

### Régime 1 — pic 130-140 mots (2000)
Distribution large (ALG, POL, GEN, ECO tous bien représentés).
Sur-représentation modérée :
- Service **BRF** (×3.16) et **BRN** (×2.53) — services régionaux courts
- Catégorie **RAN** (×9.77, faible volume)

Le format court est transversal aux sujets, légèrement tiré vers le
bas par les services régionaux.

### Régime 2 — pic 240-250 mots (2011)
Sur-représentation :
- Service **EXT** (×2.05) — dépêches internationales
- Catégorie **POL** (×1.53)

L'allongement à ~245 mots est tiré par la couverture
internationale/politique.

### Régime 3 — pic 290-300 mots (2024)
Très diffus, partagé entre les grands services :
- **EXT** (×1.39), **SPF** (×1.27), **INT** (×1.11)
- Catégorie **GEN** (×1.34)

Le format de 290 mots est la **norme partagée** par l'ensemble des
services.

### Conclusion
Les taches claires sont des **modes globaux**, pas la signature d'un
sujet précis. Le doublement du format modal est un **changement
éditorial global** de l'agence, pas un déplacement de sujets dans le
corpus.

## 4. Queue ≥790 mots et métacommunication

La queue cumulée à l'extrême droite (≥790 mots) culmine **2014-2018**
(1,3 - 1,5 % du volume annuel) :

| Année | Part queue | N queue |
|---|---|---|
| 2017 | 1,47 % | 2 954 |
| 2015 | 1,38 % | 2 840 |
| 2016 | 1,38 % | 2 895 |
| 2018 | 1,34 % | 2 900 |
| 2014 | 1,33 % | 2 627 |

Cohérent avec les artefacts de métacommunication déjà identifiés
(programmes du jour, bilans BelgaService — cf.
[metacommunication_belga.md](metacommunication_belga.md)). Le
filtrage n'affecte pas les modes principaux mais aplatit cette queue.

## 5. À retenir pour les analyses

- **Toute comparaison de longueur entre années doit prendre en compte
  les trois régimes** : un seuil « dépêche longue » fixé à 250 mots
  n'a pas le même sens en 2000 (queue) qu'en 2020 (médiane).
- Le filtrage métacomm est utile pour la queue (≥790) mais n'altère
  pas la structure modale — donc inutile pour étudier le format
  central.
- Les transitions 2010 et 2014 sont des candidates pour creuser les
  causes éditoriales (refonte de produit, nouveaux services, contrats
  clients).

## Voir aussi

- [disclaimer_belga_press.md](disclaimer_belga_press.md) — autre
  rupture éditoriale (2014, 2019)
- [metacommunication_belga.md](metacommunication_belga.md) — artefacts
  longue queue
- `code/depeches/graphiques/mots_par_depeche.py` — script de génération
