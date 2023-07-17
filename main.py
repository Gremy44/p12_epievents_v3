from controllers.start_cli import start_cli
from models.users_model import Base, User
from sqlalchemy.orm import sessionmaker
from config import engine
import datetime
from datetime import datetime
from utils.add_user import Add_user
import os
from models.users_seeder import UserSeeder

database_path = 'database\database.db'

'''# Créez une session
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

user = User(
    first_name='John',
    last_name='Doe',
    email='john.doe@example.com',
    password='my_password',
    is_active=True,
    date_created=datetime.now(),
    last_login=datetime.now(),
    role_id=1  # Remplacez 1 par l'ID du rôle approprié
)

session.add(user)
session.commit()

# Reste de votre code...
session.close()'''

if __name__ == "__main__":
    # init session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # create database if not exists
    Base.metadata.create_all(engine)
    
    # create fake user
    users_seed = UserSeeder()
    users_seed.run()
    
    # call first view
    start = start_cli()
    
    # await user input
    any = input("Press any key to close app...")
    
    # Close session
    session.close()
    
    # keep this line if you want no persistent data 
    os.remove(database_path)
