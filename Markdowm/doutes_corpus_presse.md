# Doutes sur la sélection des dépêches pour le corpus Presse

*Synthèse au 2026-05-13. Recense les incertitudes identifiées sur le **périmètre** et la **classification** des dépêches retenues dans `corpus_medias_belges_1994_2025.csv` (13 595 dépêches), filtrées depuis `depeches.duckdb` (6,3 M).*

---

## 1. Définition du périmètre — deux cas, frontières floues

Le critère retenu (cf. `feedback_perimetre_medias_belges` + `feedback_perimetre_evolution_informationnelle`) couvre **deux cas et deux seulement** :

- **Cas 1 — Le média éditorial belge est sujet frontal** : entreprise de presse, journaliste, chaîne, régulateur, déontologie, audience, restructuration, opération capitalistique, programme, publication.
- **Cas 2 — Évolution de l'écosystème informationnel belge** : sondages en ligne sur sites de quotidiens, études commandées/publiées par un média belge, comportements informationnels, nouveaux formats journalistiques.

Tout le reste — média belge comme **simple source/plateforme/vecteur** — est hors périmètre. Mais la frontière reste contestée sur plusieurs catégories de cas.

---

## 2. Pool de doute — 647 dépêches à arbitrer manuellement

Le script `generer_pool_doute.py` surface les dépêches qui matchent un des 9 patrons ambigus identifiés pendant la calibration des gold sets. **Ces 647 lignes attendent toutes une validation humaine** pour confirmer leur inclusion/exclusion.

| Code | Patron | Doute concret |
|---|---|---|
| **A** | reprise + `motcle_reprise_seul` + groupe média belge mentionné | Faux négatifs type Sanoma/Interkabel : le média est mentionné mais classé "reprise" → exclu à tort ? |
| **B** | `headline_(source)` où parenthèse = média non-belge mais keywords BELGIQUE | Ex. TV5Monde/TSR : média étranger en parenthèse, contenu belge → in ou out ? |
| **C** | sujet `defaut` — aucun signal positif détecté | Classé "sujet" faute de mieux, sans match positif → vrai positif ou bruit ? |
| **D** | headline "source d'information / étude / sondage / baromètre" mais ≠ sujet | Cas 2 du périmètre potentiellement raté |
| **E** | "a signé avec / rejoint / engagé par" + groupe belge tagué reprise | Ex. Vercauteren/RTL-Sport : RH dans groupe média belge mais classé reprise |
| **F** | "agence Belga" dans headline/extrait tagué reprise/mixte | Ex. partenariat UCL/Belga : Belga sujet mais mal classé |
| **G** | `headline_(source)` parenthèse non-belge ET non-BELGA | Ex. études Vacature : éditeur d'annuaires ≠ presse, mais ambigu |
| **H** | "dépêche / journalisme / agence de presse" + MEDIA mais ≠ sujet | Vocabulaire métajournalistique sans sujet média clair |
| **J** | démenti/réfutation/contestation info publiée par média belge | Vie déontologique — à inclure mais souvent classé "reprise" |

---

## 3. Zones grises de périmètre — règles non encore tranchées

### 3.1 Tier-2 ambigus (médias belges au nom polysémique)
`La Première`, `La Capitale`, `Pan`, etc. : un match seul **ne suffit pas**. Il faut un marqueur belge supplémentaire (ville belge, ministre belge, "belge/Belgique/flamand/wallon/bruxellois"), **sauf** si le tier-2 est un média audiovisuel/opérateur (TVi, Versatel, Belgacom, Canal+) — auquel cas le match seul qualifie.

→ **Doute** : la liste des opérateurs/médias audiovisuels « qualifiants » est-elle exhaustive ?

### 3.2 Presse étrangère diffusée en Belgique
Ex. mensuel français *See* (gold 2012 #09). À examiner **au cas par cas**, ne pas exclure automatiquement sur la seule base du pays d'origine. Proposition : signal `presse_etrangere_diffusee_be` qui pousse en `mixte` plutôt qu'exclusion.

→ **Doute** : pas de critère opérationnel actuel pour décider de la diffusion belge.

### 3.3 Médias en rôle de plateforme vs sujet
- Interview/tribune accordée par un média belge → **hors** périmètre
- Émission TV utilisée comme plateau pour annonce d'un tiers → **hors** (sauf si la dépêche parle de l'émission elle-même)
- Bande-annonce d'émission TV → **hors** (1995 #08 Controverse RTL-TVi)
- Litige télécom pur (Orange vs Telenet/VOO/Proximus) → **hors** : concurrence sans dimension éditoriale

→ **Doute** : la frontière "dimension éditoriale" reste subjective. BUG 5 (médias en rôle incidentiel) est partiellement adressé par le pool de doute (E, F, J) mais pas tranché.

### 3.4 Politique relayée par un média
Els Van Weert/VRT, Open Vld/Standaard = **hors** ("ne concerne pas les journaux"). Mais nomination Bossaert chez Medialaan = **dedans**.

→ **Doute** : la distinction tient au sujet (politique pure vs RH média), pas toujours évidente sur le headline seul.

### 3.5 Démentis et réfutations
Ford-Genk dément Het Volk (gold 1998 #54), BNP Paribas réfute Le Soir (gold 2015 #23) = **dedans** (déontologie, vie de la presse). Mais distinguer d'un simple "X dément l'info publiée par Y" sans dimension déontologique reste flou.

### 3.6 Éditeurs hors-presse
ITT-Promedia (éditeur d'annuaires téléphoniques, 1995 #21) = **hors**. Lloyd publiant l'Annuaire port Anvers (gold 1998 #59) = **dedans** (journal spécialisé).

→ **Doute** : critère "publication éditoriale" mal opérationnalisé.

### 3.7 Cas validés inclus malgré marqueurs lexicaux faibles
À ne **pas** exclure même si pattern faible :
- Nomination/licenciement de cadres média belge (même quand le nom propre est en `(parenthèses)` qui masque le sujet)
- Opérations capitalistiques sortantes (Rossel rachète à l'étranger)
- Résultats financiers d'un groupe média belge (Sanoma Belgique +15 % via VT4/VIJFtv)
- Journaliste belge interpellé/arrêté/relâché
- Colloque/formation/déontologie journalistique

---

## 4. Artefacts qui polluent ou masquent la sélection 

### 4.1 Métacommunication BELGA (~265 000 dép., 4,2 % du corpus brut)
Dépêches **non rédactionnelles** dans le flux : programmes, revues de presse internes, communiqués officiels relayés, bilans, kills, advisories. Familles concernées :
- `BelgaService%` (103 616 dép., 2006-2023) — dont **Mediawatch** qui peut être confondu avec couverture éditoriale réelle
- `PROGRAM OF THE DAY`, `BELGANIGHT`, `BELGA NEXT`, `ATTENTION USERS`
- `JOUR DD/MM` / `MONDAY DD/MM` (agendas, 2014-2023)
- `CORRECTION`/`CORRECTIE`, `KILL`, `ADVISORY`, `RECAP`/`BILAN`

→ **Doute** : ces dépêches doivent-elles être systématiquement filtrées en amont du classifier, ou certaines (revues de presse !) sont-elles précisément des sources sur l'écosystème presse ?

### 4.2 Dépêches > 800 mots = ~45 % de programmes/bilans
Records >10 000 mots concentrés 2015-2016 = bilans BelgaService, **pas** un allongement éditorial. Toute analyse de longueur sur le corpus presse est biaisée si non filtré.

### 4.3 Rupture format 2019-2020
Les tags techniques (`(PRESS)`, `BelgaService:`, `ALERT:`, préfixes sport auto) quittent le headline pour migrer vers `priority`/`categorie`. **Conséquence directe sur le corpus presse** : la corrélation `(PRESS)` ↔ disclaimer body est cassée après 2019. Le keyword `PRESS` ne se comporte pas pareil avant et après.

→ **Doute** : faut-il appliquer une stratégie hybride (`headline LIKE` + `priority`/`categorie`) dans le filtre amont `recherche_medias.py` ?

### 4.4 Disclaimer BELGA-PRESS — 4 régimes
- pré-2008 : absent
- 2008-2013 : pilote, variations textuelles
- 2014-2018 : consolidé, 1500-1800/an
- 2019+ : `(PRESS)` quitte le headline, disclaimer body reste mais orphelin (971 disclaimer_seul en 2019)

→ Le disclaimer body reste **le marqueur fiable** sur toute la période 2008+, mais le `(PRESS)` headline n'est utilisable que 2010-2019.

### 4.5 Séparateurs typographiques
`BelgaService:` est devenu `BelgaService -` en 2014. Une regex stricte fait croire à une extinction de service / de famille. **Toujours tester `:`, ` -`, ` —`, espace** avant d'exclure ou de filtrer.

---

## 5. Anomalies non clôturées sur le corpus filtré (1994-2025)

Répartition actuelle du corpus presse :

| Type | N | % |
|---|---:|---:|
| sujet | 10 524 | 77 % |
| mixte | 2 127 | 16 % |
| reprise | 856 | 6 % |
| **Total** | **13 595** | |

**Pool doute** : 647 dépêches à valider.

### Creux et bosses suspectes
- **2021 creux** : 202 dépêches vs ~450 voisines — **XMLs manquants ?** À investiguer (`Depeche_normalized/2021/`).
- **2002-2003** : reprises élevées (94, 91) — possiblement un format "Reprise de la presse" à mieux classer.
- **2007-2008** : mixte élevé (~20-30 %) **non validé** par gold set.

### Gold sets non encore validés
- 1998, 2008, 2015/2016, 2020 — pas de validation humaine de référence sur ces années.

---

## 6. Lacunes corpus source qui affectent le corpus presse

Si le XML source est absent, aucune dépêche presse ne peut être sélectionnée. À garder en tête pour toute interprétation longitudinale :

| Période | Effet sur corpus presse |
|---|---|
| 1996-06-01 → 1996-06-16 | Volume juin 1996 ÷ 2 (extrapolable) |
| 2006-07-27 → 2006-12-31 | **Second semestre 2006 quasi-absent** — 158 jours |
| 2011-06 + 2011-07 (1-25) | **Flux FR absent 55 jours** ; invisible sans ventilation par `langue` |
| 2016-08-19 → 2016-08-31 | Fin août manquante |
| 2017-10-17 → 2017-10-31 | Deuxième moitié manquante |
| 2024-01-11 → 2024-02-09 | Lacune début 2024 |
| 2025-05-23 → 2025-05-31 | Fin mai manquante |

**Baisse structurelle 2019-2025** (−21 % du taux quotidien BELGA global, cause indéterminée) : si elle frappe aussi les sujets presse, certains "creux" du corpus presse peuvent être de simples reflets de la baisse globale, pas une diminution de la couverture presse en propre.

---

## 7. BUGs classifier connus (état au 2026-05-12)

Le script `filtrer_medias_belges.py` (v3 → 2026-05-12) a corrigé 4 bugs majeurs :
- **BUG 1** : `garde_fou:telecom_pur` exemptait des dépêches avec `MEDIA`/`TV` à tort
- **BUG 2** : bulletins audience CIM → faux `headline_(source)`
- **BUG 3** : "reprise" = acquisition dans `mot_cle` → désormais routé vers `PATRON_CAPITALISTIQUE`
- **BUG 4** : `(ex-Point Culture)` → faux `headline_(source)`

Bugs résiduels :
- **BUG 5** — médias en rôle incidentiel : adressé par le pool de doute (E, F, J), pas par patch classifier
- **BUG 6** — loose matches en amont dans `recherche_medias.py` : hors scope classifier

---

## 8. Actions / arbitrages en attente

1. **Valider manuellement les 647 lignes** de `pool_doute_1994_2025.csv` (critères A-J).
2. **Construire les gold sets manquants** : 1998, 2008, 2015/2016, 2020.
3. **Investiguer le creux 2021** (202 dép.) : XMLs manquants ou vrai creux ?
4. **Trancher le statut des revues de presse** internes BelgaService Mediawatch : source ou pollution ?
5. **Trancher le statut de la presse étrangère diffusée en Belgique** : signal opérationnel à définir.
6. **Stratégie hybride headline + priority/categorie** pour récupérer les marqueurs presse post-2019.
7. **Compléter la liste des médias/opérateurs audiovisuels "qualifiants"** sans marqueur belge additionnel.

---

## Documents et mémoires liés

- `feedback_perimetre_medias_belges.md` — règles tier-2, périphérie, cas validés gold 1995/2012/2018
- `feedback_perimetre_evolution_informationnelle.md` — cas 2 (sondages/études)
- `feedback_headlines_belgaservice.md` — séparateurs typographiques
- `project_depeche_classifier_raffinement.md` — état v3 classifier + pool de doute
- `metacommunication_belga.md` — typologie complète des artefacts à filtrer
- `project_depeche_rupture_format_2020.md` — rupture headline → champs structurés
- `project_disclaimer_belga_evolution.md` — 4 régimes du disclaimer
- `docs/depeches/audit/audit_mois_suspects.md` — lacunes corpus source
- `code/depeches/recherche/filtrer_medias_belges.py` — classifier courant
- `code/depeches/recherche/generer_pool_doute.py` — extraction des 9 critères
