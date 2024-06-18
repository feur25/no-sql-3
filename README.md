Atelier 2 - Liaison SGBDR & Elasticsearch
Ce guide détaille les étapes pour mettre en place un environnement où Elasticsearch est utilisé comme moteur d'indexation devant une base de données relationnelle. Cela permettra de faciliter la mise en œuvre de services comme un moteur de recherche de produits à partir des données stockées dans la base de données relationnelle.

Partie 1: Installation et Configuration du SGBDR & Peuplement des Données
Choix de l'Environnement
Vous avez choisi de configurer les services dans des conteneurs Docker pour une portabilité et une gestion simplifiée.
Installation du SGBDR (PostgreSQL)

    docker-compose up -d postgres

Création de Données Fictives
Utilisation d'un script Python (populate_data.py) pour générer et insérer des données fictives dans PostgreSQL.

    python populate_data.py

Validation
Vérifiez que les données sont correctement insérées dans PostgreSQL en exécutant des requêtes depuis le client PostgreSQL.

    docker-compose exec postgres psql -U user -d mydatabase

    SELECT * FROM products;
Partie 2: Synchronisation des Données du SGBDR avec Elasticsearch
Installation de Logstash

    docker-compose up -d logstash

Configuration du Pipeline de Données (Logstash)
Utilisation d'un fichier de configuration logstash.conf pour définir la récupération des données depuis PostgreSQL et leur envoi vers Elasticsearch.
Validation
Vérifiez que les données sont correctement indexées dans Elasticsearch.

    curl -X GET "localhost:9200/"

Structure des Fichiers
docker-compose.yml: Définition des services PostgreSQL, Elasticsearch, et Logstash.
populate_data.py: Script Python pour générer des données fictives et les insérer dans PostgreSQL.
logstash.conf: Configuration de Logstash pour le pipeline de données depuis PostgreSQL vers Elasticsearch.
Prérequis 
Docker et Docker Compose installés sur votre système.
Python (pour exécuter populate_data.py).
Remarques
Assurez-vous que les ports 5432 (PostgreSQL), 9200 (Elasticsearch) et 5044 (Logstash) ne sont pas utilisés par d'autres applications sur votre système.
L'environnement utilise des images Docker officielles pour PostgreSQL, Elasticsearch et Logstash.
Le script Python populate_data.py utilise Faker pour générer des données fictives dans la table products de PostgreSQL.
Améliorations Futures
Ajouter une interface utilisateur pour interroger Elasticsearch.
Configurer une stratégie de sauvegarde pour les données Elasticsearch.
Utiliser Kibana pour visualiser et explorer les données indexées.
