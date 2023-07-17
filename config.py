from sqlalchemy import create_engine

# Spécifiez l'URL de connexion SQLite
database_url = 'sqlite:///database/database.db'

# Créez le moteur de base de données
engine = create_engine(database_url)

