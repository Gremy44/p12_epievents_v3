from controllers.login_controller import Login_Controller
from models.users_model import Base, User, Role
from models.customers_model import Customer
from models.contracts_model import Contract
from models.events_model import Event
from sqlalchemy.orm import sessionmaker
from config import engine, Session
import os
from models.seeders.users_seeder import UserSeeder
from models.seeders.customers_seeder import CustomerSeeder
from models.seeders.events_seeder import EventSeeder
from models.seeders.contracts_seeder import ContractSeeder
from router.router import Console
from datetime import datetime


database_path = 'database\database.db'

class Start_Cli:
    
    def __init__(self):
        pass
    
    def start_cli_dev_mod():
        '''
        Dev mode with no persistent data
        '''
        os.remove(database_path)
        
        # create session
        session = Session()
        
        # create database if not exists
        Base.metadata.create_all(engine, tables=[Role.__table__,
                                                 User.__table__,
                                                 Customer.__table__,
                                                 Contract.__table__,
                                                 Event.__table__])
        
        # create fake user
        users_seed = UserSeeder(session)
        users_seed.run()
        
        #create fake customers
        customers_seed = CustomerSeeder(session)
        customers_seed.run()
        
        events_seed = EventSeeder(session)
        events_seed.run()
        
        contracts_seed = ContractSeeder(session)
        contracts_seed.run()
        
        create_role_sale = Role(
            role = 'Sale'
        )
        
        create_role_support = Role(
            role ='Support'
        )
        
        create_role_gestion = Role(
            role ='Gestion'
        )
        
        create_admin = User(
            first_name='admin',
            last_name='admin',
            email='admin@email.com',
            password=('admin'),
            is_superuser = True,
            date_created=datetime.now(),
            last_login=datetime.now()
        )
        
        create_user = User(
            first_name='Jean',
            last_name='Lambda',
            email='jl@email.com',
            password=('S3cret!'),
            is_superuser = False,
            date_created=datetime.now(),
            last_login=datetime.now(),
            role_id=1
        )
        
        session.add(create_role_sale)
        session.add(create_role_support)
        session.add(create_role_gestion)
        session.add(create_admin)
        session.add(create_user)
        session.commit()
        
        router = Console()
        router.routing()
        
        # await user input
        any = input("Press any key to close app...")
        
        # close session
        session.close()
        
        # delete database
        os.remove(database_path)