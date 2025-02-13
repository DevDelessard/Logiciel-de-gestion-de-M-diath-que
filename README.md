Logiciel de gestion de Médiathèque

📌 Description du projet

Ce projet est une application de gestion de médiathèque permettant aux bibliothécaires de gérer les membres et les emprunts de médias (livres, DVD, CD, jeux de plateau). Il inclut également une interface pour les membres afin qu'ils puissent consulter les médias disponibles.

🛠 Technologies utilisées

Python 3

Django

SQLite (base de données par défaut)

HTML / CSS pour l'affichage des pages

🚀 Installation et exécution du projet

1️⃣ Cloner le projet

git clone https://github.com/DevDelessard/Logiciel-de-gestion-de-M-diath-que.git
cd Logiciel-de-gestion-de-M-diath-que

2️⃣ Exécuter l'application sans installation préalable

Si vous ne souhaitez pas configurer d’environnement, vous pouvez utiliser Python directement :

python3 manage.py runserver

Puis, ouvrez un navigateur et accédez à :

http://127.0.0.1:8000/

3️⃣ Accéder aux fonctionnalités

Connexion bibliothécaire : permet d'accéder aux fonctionnalités de gestion

Gestion des membres : ajouter, modifier et supprimer des membres

Gestion des médias : ajouter, modifier et supprimer des livres, CD, DVD et jeux de plateau

Emprunts et retours : enregistrer un emprunt et le restituer

Consultation publique : voir la liste des médias disponibles

📂 Organisation des fichiers

|-- bibliotheque/
    |-- models.py   # Modèles de la base de données
    |-- views.py    # Logique métier et affichage
    |-- urls.py     # Routes de l'application
    |-- tests.py    # Tests unitaires
|-- templates/
    |-- *.html      # Pages de l'application
|-- db.sqlite3      # Base de données SQLite
|-- manage.py       # Gestionnaire Django

🧪 Exécuter les tests

Pour s'assurer que tout fonctionne correctement :

python3 manage.py test bibliotheque

📌 Auteur

👤 DevDelessard - Projet réalisé dans le cadre du Centre Européen de Formation

✨ Merci d'utiliser ce logiciel ! 😊
