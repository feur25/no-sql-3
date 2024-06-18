import psycopg2
from faker import Faker

# Connexion à la base de données
conn = psycopg2.connect(
    dbname="mydatabase",
    user="user",
    password="password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Utilisation de Faker pour générer des données fictives
fake = Faker()

# Insertion des données fictives dans la table products
for _ in range(100):  # Générer 100 enregistrements
    name = fake.word().capitalize() + " " + fake.word().capitalize()
    description = fake.text()
    price = round(fake.random_number(digits=2), 2)
    cursor.execute(
        "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)",
        (name, description, price)
    )

# Validation et fermeture de la connexion
conn.commit()
cursor.close()
conn.close()
