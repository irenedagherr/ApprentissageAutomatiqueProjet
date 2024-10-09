# Prédiction de la qualité des soudures

<img width="1180" alt="Screenshot" src="Screenshot 2024-10-08 at 21.41.45.png">

*English version available below* 

## Description

Ce projet vise à prédire la qualité des soudures sur des aciers en utilisant des données publiques issues de Welddb [(Welddb)](https://www.phase-trans.msm.cam.ac.uk/map/data/materials/welddb-b.html). En automatisant l'évaluation de la qualité des soudures à l'aide de techniques de machine learning, nous cherchons à extraire des connaissances des données disponibles afin d’identifier des modèles nouveaux qui pourraient améliorer la qualité des soudures. La qualité des soudures est un facteur essentiel pour de nombreux secteurs industriels, notamment dans les industries aérospatiale, automobile et de la construction.

## Objectif

La qualité des soudures est difficile à quantifier, car elle repose souvent sur l’*expertise humaine* et la *transmission des savoirs entre soudeurs expérimentés*. Cela rend l'évaluation subjective et dépendante d'avis d'experts, ce qui peut entraîner des incohérences et des erreurs dans le processus de contrôle qualité. Ce projet a pour but de trouver des solutions basées sur des modèles d'apprentissage automatique supervisés, non supervisés et semi-supervisés pour identifier les facteurs clés qui définissent une bonne soudure, et fournir ainsi des outils aux industriels pour améliorer la fiabilité et l'efficacité de leur production.

## Collaborateurs

- [@irenedagherr](https://github.com/irenedagherr)
- [@anthony-qtn](https://github.com/anthony-qtn)
- [@nancy-222](https://github.com/nancy-222)

## Détails supplémentaires

Le projet est développé en *Python* avec des notebooks *Jupyter* (.ipynb), une plateforme idéale pour l'exploration de données et le développement de modèles de machine learning.

## Organisation

On retrouve dans ce fichier les dossiers suivants :

1. InformationsPubliques : Contenant les fichiers trouvés via le lien, c'est-à-dire les données publiques.
2. GetData : Prise en main du fichier et nettoyage de la base de données.
3. Preprocessing : Étapes de prétraitement ainsi que l'analyse descriptive.
4. Dataset : Contient les fichiers avec extension .csv.
5. ImplementationML : Les méthodes (modèles), métriques et comparaisons.

## Installation

Pour exécuter le projet localement, suivez ces étapes :

1. Installez Python depuis [python.org](https://www.python.org/downloads/).
2. Installez Jupyter Notebook en exécutant la commande suivante :  
   *pip install notebook*
3. Naviguez dans le dossier du projet et ouvrez le fichier .ipynb avec Jupyter Notebook
4. Installez les dépendances requises en exécutant le fichier requirements.txt 
   
Vous êtes maintenant prêt à explorer les modèles de prédiction de la qualité des soudures et à ajuster les paramètres pour optimiser les résultats.

## Statut du projet

Objectifs atteints :

- Utilisation d'algorithmes supervisés, non supervisés et semi-supervisés.
- Pré-traitement des données de soudure issues de Welddb.
- Développement de modèles prédictifs pour la qualité des soudures.
- Acquisition de compétences en apprentissage automatique.

*Nous accueillons les retours et contributions de la communauté ! Si vous rencontrez des problèmes ou avez des suggestions, veuillez nous contacter directement*.




# Weld Quality Prediction

## Description

This project aims to predict the quality of welds on steel using public data from Welddb [(Welddb)](https://www.phase-trans.msm.cam.ac.uk/map/data/materials/welddb-b.html). By automating the evaluation of weld quality using machine learning techniques, we seek to extract insights from the available data to identify new patterns that could improve weld quality. The quality of welds is a critical factor for many industrial sectors, particularly in aerospace, automotive, and construction industries.

## Purpose

Weld quality is difficult to quantify because it often relies on *human expertise* and the *transfer of knowledge among experienced welders*. This makes the assessment subjective and dependent on expert opinions, which can lead to inconsistencies and errors in the quality control process. This project aims to find solutions based on supervised, unsupervised, and semi-supervised machine learning models to identify key factors that define a good weld, thus providing tools to industries to improve the reliability and efficiency of their production.

## Collaborators

- [@irenedagherr](https://github.com/irenedagherr)
- [@anthony-qtn](https://github.com/anthony-qtn)
- [@nancy-222](https://github.com/nancy-222)

## More Details

The project is developed in *Python* using *Jupyter* notebooks (.ipynb), an ideal platform for data exploration and the development of machine learning models.

## Organisation

This file contains the following folders:

1. PublicInformation: Contains the files found through the provided link, i.e., the public data.
2. GetData: Data retrieval and initial cleaning of the dataset.
3. Preprocessing: Preprocessing steps as well as descriptive analysis.
4. Dataset: Contains files in .csv format.
5. ImplementationML: The methods (models), metrics, and comparisons.

## Installation

To run the project locally, follow these steps:

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install Jupyter Notebook by running the following command:  
   *pip install notebook*
3. Navigate to the project folder and open the .ipynb file with Jupyter Notebook.
4. Install the required dependencies by executing the requirements.txt file:

You are now ready to explore the weld quality prediction models and fine-tune the parameters to optimize the results.

## Project Status

Milestones achieved:

- Applied supervised, unsupervised, and semi-supervised algorithms.
- Preprocessed welding data from Welddb.
- Developed predictive models for weld quality.
- Gained expertise in machine learning.

*We welcome feedback and contributions from the community! If you encounter any issues or have suggestions, please feel free to reach out directly.*

