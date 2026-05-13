# Évolution du disclaimer BELGA-PRESS dans les dépêches

Analyse longitudinale du disclaimer « Belga diffuse quotidiennement des
dépêches reprenant… » sur `depeches.duckdb` (1994-2026).
Session du 2026-05-12.

## 1. Apparition et formule originelle

Première occurrence : **6 mai 2008**.

Formule d'origine :
> Belga diffuse quotidiennement des dépêches reprenant des informations
> **intéressantes** provenant d'autres **media** […]. Belga ne peut
> toutefois **jamais** être tenu pour responsable […].

Avant 2008 : pas de disclaimer dans le corpus.

## 2. Mutations textuelles

Trois mutations successives du texte, espacées dans le temps :

| # | Changement | Période de bascule |
|---|---|---|
| 1 | `intéressantes` → supprimé | transition 2008 → 2009 |
| 2 | `media` → `médias` | courant 2010 (10/284) |
| 3 | `ne peut jamais` → `ne peut pas` | courant 2013 (50/265) |

À partir de 2014, le texte se stabilise.

## 3. Volumes par période

Disclaimer canonique (toutes variantes textuelles confondues) :

| Période | Régime | Volume annuel |
|---|---|---|
| 2008-2013 | Pilote, variations textuelles | 188 – 318 |
| 2014 | Systématisation (× 4) | 1 417 |
| 2014-2018 | Pic consolidé | 1 500 – 1 800 |
| 2019-2020 | Déclin marqué | 1 538 → 1 322 |
| 2021-2025 | Régime bas stable | 600 – 1 000 |
| 2026 (jan-mai) | Partiel | 65 |

## 4. Lien avec la convention `(PRESS)` en headline

Le tag `(PRESS)` dans le headline précède chronologiquement l'apparition
du disclaimer (premiers cas 2004-2007, explosion en 2010 à 7 311 —
possible anomalie pipeline à vérifier).

Relation des deux marqueurs :

- **2010** : 7 066 dépêches `(PRESS)` SANS disclaimer body
- **2012-2018** : ~99 % des dépêches `(PRESS)` portent aussi le
  disclaimer body — les deux marqueurs sont alignés
- **2019-2020** : **rupture de format**. Le tag `(PRESS)` quitte le
  headline (3 797 → 1 405), mais le disclaimer body reste — 971
  dépêches « disclaimer seul » en 2019.

Cette rupture est cohérente avec la migration plus générale des tags
techniques du headline vers les champs `priority` / `categorie`
documentée par ailleurs (voir
[plan_normalisation.md](plan_normalisation.md) et le memo
`project_depeche_rupture_format_2020`).

## 5. Quatre régimes à distinguer pour les analyses longitudinales

Pour toute analyse portant sur le headline ou le keyword PRESS,
séparer en quatre régimes :

1. **Pré-2008** — pas de disclaimer
2. **2008-2013** — pilote, variations textuelles successives
3. **2014-2018** — consolidé, texte stable, volume haut
4. **2019+** — rupture format : disclaimer body reste, `(PRESS)`
   headline s'efface

Le **disclaimer body** est un marqueur fiable de relais d'information
externe sur toute la période 2008+. Le **tag `(PRESS)` headline** ne
l'est que jusqu'en 2018.
