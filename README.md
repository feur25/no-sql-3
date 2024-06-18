### $${\color{red}Travail \space en \space équipe \space avec :}$$
$${\color{lightgreen}Giromagny \space Alexis / Pham \space Guillaume / Axel \space Sevenet / Valentin \space Chorro}$$
# Atelier 2 - Liaison SGBDR & Elasticsearch

Ce guide détaille les étapes pour mettre en place un environnement où Elasticsearch est utilisé comme moteur d'indexation devant une base de données relationnelle. Cela permettra de faciliter la mise en œuvre de services comme un moteur de recherche de produits à partir des données stockées dans la base de données relationnelle.

# Partie 1: 

Installation et Configuration du SGBDR & Peuplement des Données

Installer le fichier requirements :

    pip3 install -r requirements.txt
    
Choix de l'Environnement
Vous avez choisi de configurer les services dans des conteneurs Docker pour une portabilité et une gestion simplifiée.
Installation du SGBDR (PostgreSQL)

    docker-compose up -d postgres
    
Vous pouvez maintenant accéder au conteneur PostgreSQL et créer une table.

    docker exec -it <container_id> psql -U user -d mydatabase

    CREATE TABLE products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        description TEXT,
        price DECIMAL(10, 2),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

Création de Données Fictives
Personellement dans cette partie, nous avons ouvert un autre terminale pour générer les données fictives via le script python.
<img width="1018" alt="Capture d’écran 2024-06-18 à 15 22 05" src="https://github.com/feur25/no-sql-3/assets/39668417/042a4015-bcf1-473a-8f84-6f87f31f4e75">

Utilisation d'un script Python (populate_data.py) pour générer et insérer des données fictives dans PostgreSQL.

    python populate_data.py

<img width="1018" alt="Capture d’écran 2024-06-18 à 15 22 05 1" src="https://github.com/feur25/no-sql-3/assets/39668417/fd81988a-f071-4851-af36-436e6cb590dc">

Validation
Vérifiez que les données sont correctement insérées dans PostgreSQL en exécutant des requêtes depuis le client PostgreSQL.

    docker-compose exec postgres psql -U user -d mydatabase

    SELECT * FROM products;


<img width="950" alt="Capture d’écran 2024-06-18 à 15 24 04" src="https://github.com/feur25/no-sql-3/assets/39668417/c5e81ca8-00ae-484e-bcc0-a3c5141f5d37">

# Partie 2: Synchronisation des Données du SGBDR avec Elasticsearch

Installation de Logstash

    docker-compose up -d logstash

Configuration du Pipeline de Données (Logstash)
Utilisation d'un fichier de configuration logstash.conf pour définir la récupération des données depuis PostgreSQL et leur envoi vers Elasticsearch.
Validation
Vérifiez que les données sont correctement indexées dans Elasticsearch.

    curl -X GET "localhost:9200/"


<img width="541" alt="Capture d’écran 2024-06-18 à 15 16 45" src="https://github.com/feur25/no-sql-3/assets/39668417/dcfee22c-2c4f-485e-bdab-c7456db2be41">

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
