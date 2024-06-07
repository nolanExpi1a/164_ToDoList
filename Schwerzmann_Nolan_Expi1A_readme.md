# Installation de votre projet

## Prérequis
1. Python 3.x
2. Pipenv
3. MySQL

## Étapes d'installation
1. Cloner le repository:
    ```
    git clone <https://github.com/nolanExpi1a/164_ToDoList.git>
    ```
2. Naviguer dans le dossier du projet:
    ```
    cd <164_ToDoList>
    ```
3. Installer les dépendances:
    ```
    pipenv install 
    ```
4. Créer un fichier `.env` avec les configurations de la base de données:
    ```
    DATABASE_URL=mysql+pymysql://<user>:<password>@<host>:<port>/<database>
    ```
5. Initialiser la base de données:
    ```
    pipenv run flask db init
    pipenv run flask db migrate
    pipenv run flask db upgrade
    ```
6. Lancer l'application:
    ```
    pipenv run flask run
    ```
