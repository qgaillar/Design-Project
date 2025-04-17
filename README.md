# Design Project – Simulation des Émissions sur le Boulevard Périphérique Parisien

Ce projet vise à modéliser les émissions de gaz à effet de serre ($CO_2$, $NO_x$, $PM_{10}$) sur le boulevard périphérique parisien en fonction de différents scénarios de mobilité (réduction de vitesse, covoiturage, etc.), à l’aide d’une interface interactive développée en Python avec `ipywidgets`.

## Lancer la simulation interactive

Clique ici pour lancer l'application web :

[![Launch Voilà](https://img.shields.io/badge/Launch%20App-Render-orange?logo=voila)](https://design-project-erl7.onrender.com)

> ⚠️ Le démarrage peut prendre quelques secondes à froid (mise en veille automatique sur Render Free Tier)

## Lancer localement

Assurez-vous d’avoir Python 3.10+ et les dépendances installées (voir `requirements.txt`), puis exécutez :

```bash
voila Modele_Simulation/Modele_Simulation_Peripherique_Parisien.ipynb


## Contenu du dépôt Github

```
Design-Project/
├── Analyse_type_vehicule_periph/
│   ├── compo_trafic.ipynb
│   ├── compositions-du-trafic-2.csv
│   ├── freq_tranche_horaire.png
│   └── newplot.png
├── Modele_Simulation/
│   ├── Ancien_modele/
│   │   └── model.ipynb
│   └── Modele_Simulation_Peripherique_Parisien.ipynb
├── voila/
│   └── voila.json
├── .render.yaml
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
├── setup.sh
└── start.py
```