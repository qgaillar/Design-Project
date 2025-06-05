# Design Project – Simulation des Émissions sur le Boulevard Périphérique Parisien

Ce projet vise à modéliser les émissions de gaz à effet de serre ($CO_2$, $NO_x$, $PM_{10}$, $PM_{2.5}$) sur le boulevard périphérique parisien en fonction de différents scénarios de mobilité (réduction de vitesse, covoiturage, etc.), à l’aide de modèles numériques développés en Python.

Deux modèles sont à disposition :

- **Modèle principal actuel** : `Modele_Simulation_A_Partir_Comptage_BP.ipynb`, basé sur les comptages réels de trafic et les profils horaires.
- **Ancien modèle interactif** : `Modele_Simulation_Peripherique_Parisien.ipynb`, utilisé via Voilà et Render, lancé à partir d'une logique entièrement théorique. (/!\ Attention ce modèle est obsolète et n'est plus mis à jour)

## Lancer la simulation interactive

L'ancien modèle est encore disponible via une interface web :

[![Launch Voilà](https://img.shields.io/badge/Launch%20App-Render-orange?logo=voila)](https://design-project-erl7.onrender.com)

> ⚠️ Le démarrage peut prendre quelques secondes à froid (Render Free Tier)

## Lancer localement

Assurez-vous d’avoir Python 3.10+ et les dépendances installées (voir `requirements.txt`), puis exécutez :

```bash
voila Modele_Simulation/Modele_Simulation_Peripherique_Parisien.ipynb
```
## Organisation du dépôt Github

``` 
Design-Project/
├── Analyse_type_vehicule_periph/
│   ├── compo_trafic.ipynb
│   ├── compositions-du-trafic-2.csv
│   ├── freq_tranche_horaire.png
│   └── newplot.png
├── Comparaison_données_actuelles/
│   ├── comparaison_airparif.ipynb
│   └── data/
│       ├── NO2/
│       ├── PM10/
│       └── PM25/
├── Modele_Simulation/
│   ├── Ancien_modele/
│   │   └── model.ipynb
│   ├── Modele_Simulation_Peripherique_Parisien.ipynb   # Ancien modèle
│   └── Modele_Emissions_Polluants_A_Partir_Comptages_BP.ipynb    # Nouveau modèle principal
├── voila/
│   └── voila.json
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
├── setup.sh
└── start.py
```