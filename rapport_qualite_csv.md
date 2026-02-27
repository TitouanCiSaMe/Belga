# Rapport qualité — Annuaires de la Presse Belge
**Date :** 27 février 2026
**Périmètre :** 24 fichiers CSV (1899–1960), hors fichiers fusionnés
**Total lignes :** 9 009 → 9 006 après nettoyage

---

## 1. Vue d'ensemble des fichiers

| Annuaire | Lignes | Colonnes réelles | Statut |
|---|---:|---:|---|
| 1899 | 270 | 10 | ✅ Complet |
| 1900-1901 | 305 | 11 | ✅ Complet |
| 1902 | 319 | 11 | ✅ Complet |
| 1903 | 330 | 11 | ✅ Complet |
| 1904 | 296 | 10 | ✅ Complet |
| 1905 | 301 | 10 | ✅ Complet |
| 1906 | 298 | 10 | ✅ Complet |
| **1907** | **252** | 10 | ⚠️ Incomplet (intitulé « à refaire ») |
| 1908 | 308 | 10 | ✅ Complet |
| 1909 | 310 | 10 | ✅ Complet |
| 1910 | 321 | 10 | ✅ Complet |
| 1911 | 315 | 10 | ✅ Complet |
| 1912 | 328 | 10 | ✅ Complet |
| 1913 | 338 | 10 | ✅ Complet |
| 1920-1921 | 368 | 11 | ✅ Complet |
| 1922-1923 | 356 | 11 | ✅ Complet |
| 1926 | 406 | 11 | ✅ Complet |
| 1929-1930 | 461 | 11 | ✅ Complet (colonne Décédé vide) |
| **1933** | **127** | 11 | 🔴 Fortement incomplet (~75 % manquant) |
| 1937-1938 | 531 | 10 | ✅ Complet (colonne Décédé vide) |
| 1949-1950 | 451 | 11 | ✅ Complet |
| 1955 | 673 | 10 | ✅ Complet (colonne Décédé vide) |
| 1957-1958 | 652 | 11 | ✅ Complet (colonne Décédé vide) |
| 1960 | 693 | 10 | ✅ Complet |

**Moyenne lignes par fichier :** 375
**Fichiers sous 60 % de la moyenne :** 1933 (127), 1907 (252)

---

## 2. Fichiers à reprendre depuis le PDF source

### 2.1 Annuaire 1933 — Saisie tronquée 🔴

C'est le cas le plus critique. Avec seulement **127 lignes**, ce fichier est très en-deçà des annuaires voisins (461 lignes en 1929-1930, 531 en 1937-1938). L'analyse de la répartition alphabétique révèle que seules les premières pages du PDF ont été saisies.

**Répartition alphabétique dans 1933 vs 1929-1930 :**

| Lettre | 1933 | 1929-1930 | Écart |
|:---:|---:|---:|---:|
| A | 8 | 9 | ≈ normal |
| B | 47 | 56 | ≈ normal |
| C | 22 | 41 | partiel |
| D | 24 | 77 | partiel |
| E | 0 | 5 | **absent** |
| F | 6 | 18 | très partiel |
| G | 3 | 31 | **quasi-absent** |
| H | 4 | 28 | **quasi-absent** |
| I–K | 0 | 13 | **absents** |
| L | 2 | 25 | **quasi-absent** |
| M | 3 | 20 | **quasi-absent** |
| N–Q | 0 | 34 | **absents** |
| R | 1 | 24 | **quasi-absent** |
| S | 0 | 21 | **absent** |
| T | 1 | 14 | **quasi-absent** |
| U | 0 | 1 | absent |
| V | 2 | 37 | **quasi-absent** |
| W | 0 | 6 | **absent** |
| Z | 1 | 1 | normal |

> **Estimation :** environ **350 journalistes manquants**, soit ~75 % du fichier.
> **Action requise :** reprendre la saisie depuis le PDF `1933.pdf` à partir de la lettre C/D.

---

### 2.2 Annuaire 1907 — Partiellement incomplet ⚠️

Le fichier est lui-même nommé **« 1907 - à refaire »**, signalant une saisie incomplète ou incorrecte. Avec **252 lignes**, il est sensiblement en dessous des années encadrantes :

| Annuaire | Lignes |
|---|---:|
| 1906 | 298 |
| **1907** | **252** |
| 1908 | 308 |
| 1909 | 310 |

Toutes les colonnes sont remplies à 100 % : il ne manque pas de cellules, mais des **lignes entières** (~50 à 60 personnes d'après les voisins).

> **Action requise :** vérifier le PDF `1907.pdf` et compléter ou resaisir.

---

## 3. Colonnes non renseignées (délibérément vides)

Ces colonnes ont été créées dans le fichier mais n'ont jamais été remplies. Ce n'est pas une erreur de structure — c'est une information qui n'a pas été saisie, probablement parce qu'elle n'apparaissait pas clairement dans le PDF source.

### 3.1 Colonne `Décédé` — 4 fichiers à 0 %

| Annuaire | Taux de remplissage |
|---|:---:|
| 1929-1930 | 0 % |
| 1937-1938 | 0 % |
| 1955 | 0 % |
| 1957-1958 | 0 % |
| 1960 | 5 % (quelques entrées) |

> L'information peut exister dans les PDFs correspondants sous forme de symbole (†) ou de mention explicite. À compléter si nécessaire pour la cohérence du fichier fusionné.

### 3.2 Colonne `Citation(s)` — 3 fichiers à 0 %

| Annuaire | Taux de remplissage |
|---|:---:|
| 1900-1901 | 0 % |
| 1902 | 0 % |
| 1903 | 0 % |

> La colonne a été créée lors de la saisie de 1902 et 1903 (qui contiennent des citations), mais aucune valeur n'a été saisie dans 1900-1901. À vérifier si le PDF source en contient.

---

## 4. Colonnes partiellement remplies

Ces colonnes ne sont ni vides ni complètes — le faible taux peut refléter un manque d'information dans le PDF source (tous les journalistes n'ont pas de fonction listée).

| Annuaire | Colonne | Taux | Interprétation probable |
|---|---|:---:|---|
| 1960 | Fonction | 28 % | PDF peu détaillé sur les fonctions |
| 1957-1958 | Fonction | 44 % | Idem |
| 1955 | Fonction | 70 % | Acceptable |

---

## 5. Anomalies de structure corrigées

Ces anomalies ont été détectées et corrigées par les scripts d'harmonisation.

| Fichier | Anomalie | Correction appliquée |
|---|---|---|
| 1900-1901 | Titre du document sur la ligne 1, en-têtes à la ligne 3 | Skip 2 lignes au chargement |
| 1905 | Idem | Skip 2 lignes au chargement |
| 1922-1923 | Idem | Skip 2 lignes au chargement |
| 1899 | Colonnes vides nommées `Colonne1`…`ColonneN` | Ignorées au chargement |

---

## 6. Harmonisation des colonnes

Avant harmonisation, aucune colonne n'était identique dans tous les fichiers. Le tableau ci-dessous résume les familles de colonnes renommées vers un schéma commun.

| Colonne standardisée | Variantes trouvées |
|---|---|
| `Journal` | `Journal(aux) Principal(aux)`, `Journal (Affiliation)` |
| `Fonction` | `Fonction dans le journal`, `Fonction dans le journal (si connue)`, `Fonction dans le journal si connue` |
| `Comité` | `Comité dont ils sont membres`, `Comité(s) dont ils sont membres`, `Comité(s) et Section(s)`, `Comité/Membre`, `Comités/Organismes dont le journaliste est membre`, `Comité dont ils sont membres / Fonction spécifique` |
| `Statut` | `Statut de Membre`, `Statut (Type de Membre)`, `Statut (Fonction)`, `Statut (Type de Membre / Fonction)`, `Statut (Fonction/Décoration)`, `Statut (Type de Membre / Fonction / Décoration)`, `Statut (Honoraire / Effectif / Adhérent)`, `Membre Honoraire / Fonction`, `Membre Honoraire / Fonction (si indiqué)`, `Membres honoraires (Fonction)`, `Membre Honoraire (ou d'Honneur)`, `Membre Honoraire/Statut`, `Membre Statut` |
| `Annuaire (Date)` | `Annuaire`, `Annuaire (Date d'adhésion)`, `Date de l'annuaire` |
| `Décédé` | `Décédé (Oui/Non)`, `Décédé (1904)`, `Décédé ($\dagger$) / Date de décès`, `Décédé (Date)` |
| `Section` | `Section(s)`, `Section(s) d'apparition (détaillée)` |

**Résultat :** 13 colonnes standardisées identiques dans tous les fichiers harmonisés :
`Nom · Prénom · Adresse · Ville · Journal · Fonction · Comité · Statut · Annuaire (Date) · Décédé · Section · Citation(s) · Source`

---

## 7. Dédoublonnage

### 7.1 Doublons intra-annuaire
**3 doublons stricts** supprimés (même nom + prénom dans le même fichier CSV).

### 7.2 Variantes orthographiques
**425 variantes orthographiques** normalisées vers une forme canonique (choisie par fréquence d'apparition, puis richesse en accents).

Exemples représentatifs :

| Variantes trouvées | Forme canonique retenue |
|---|---|
| `EMILE` / `ÉMILE` | `Émile` |
| `BLEROT` / `BLÉROT` | `Blérot` |
| `MALLIÉ` / `MALLIE` / `Mallié` | `Mallié` |
| `CLEMENT` / `Clément` | `Clément` |
| `BUFQUIN DES ESSARTS` / `BUFQUIN des ESSARTS` | `Bufquin des Essarts` |
| `DE PENARANDA DE FRANCHIMONT` / `DE PEÑARANDA DE FRANCHIMONT` | `DE PEÑARANDA DE FRANCHIMONT` |

> **Note :** deux entrées potentiellement identiques subsistent et nécessitent une vérification manuelle : `DE LAISSÉ, Léon` et `DÉLAISSÉ, Léon` (variante avec/sans espace dans le nom).

### 7.3 Présences inter-annuaires (longitudinal)
Ces présences multiples sont **normales et souhaitées** — elles tracent les carrières dans le temps.

| Indicateur | Valeur |
|---|---:|
| Lignes totales (après nettoyage) | 9 006 |
| Journalistes uniques | 2 730 |
| Présents dans 1 seul annuaire | 1 246 |
| Présents dans 2 annuaires ou plus | 1 484 |
| Maximum (Léon Lebrun, 1900–1957) | 22 annuaires |

---

## 8. Fichiers produits

| Fichier | Description |
|---|---|
| `Excels/harmonises/*.csv` | 24 CSV individuels avec colonnes standardisées |
| `Excels/Annuaires_fusionnes_harmonises.csv` | Fusion brute harmonisée (9 009 lignes) |
| `Excels/Annuaires_fusionnes_nettoye.csv` | Fusion nettoyée + `personne_id` (9 006 lignes) |
| `Excels/journalistes.csv` | Table maître : 1 ligne par journaliste unique (2 730 lignes) |
| `Excels/harmoniser.py` | Script d'harmonisation des colonnes |
| `Excels/deduplication.py` | Script de dédoublonnage et construction de la table journalistes |

---

## 9. Actions prioritaires recommandées

| Priorité | Action | Fichier concerné |
|:---:|---|---|
| 🔴 1 | Compléter la saisie depuis le PDF (lettres C–Z manquantes) | `1933.csv` |
| ⚠️ 2 | Vérifier et compléter la saisie depuis le PDF | `1907.csv` |
| 3 | Remplir la colonne `Décédé` si info disponible dans les PDFs | `1929-1930`, `1937-1938`, `1955`, `1957-1958` |
| 4 | Vérifier si des citations existent dans le PDF | `1900-1901.csv` |
| 5 | Vérifier manuellement : `DE LAISSÉ` vs `DÉLAISSÉ` | `journalistes.csv` |
