from models.users_model import Base, User, Role
from models.customers_model import Customer
from models.contracts_model import Contract
from models.events_model import Event

from models.seeders.users_seeder import UserSeeder
from models.seeders.customers_seeder import CustomerSeeder
from models.seeders.events_seeder import EventSeeder
from models.seeders.contracts_seeder import ContractSeeder

from router.router import Console

from config import engine, Session
from utils.utils import Utils

from sqlalchemy import exc as sa_exc
from sentry_config import call_centry

from datetime import datetime
import warnings
import os


class Start_Cli:
    def __init__(self):
        pass

    def start_cli_dev_mod():
        """
        Dev mode with no persistent data
        """
        # call sentry
        call_centry()

        # Supprimer les avertissements SAWarning
        warnings.filterwarnings("ignore", category=sa_exc.SAWarning)

        database_path = "database/database.db"

        if os.path.isfile(database_path):
            os.remove(database_path)

        # create session
        session = Session()

        # create database if not exists
        Base.metadata.create_all(
            engine,
            tables=[
                Role.__table__,
                User.__table__,
                Customer.__table__,
                Contract.__table__,
                Event.__table__,
            ],
        )

        # create fake user
        users_seed = UserSeeder(session)
        users_seed.run()

        # create fake customers
        customers_seed = CustomerSeeder(session)
        customers_seed.run()

        events_seed = EventSeeder(session)
        events_seed.run()

        contracts_seed = ContractSeeder(session)
        contracts_seed.run()

        create_role_sale = Role(role="Sale")

        create_role_support = Role(role="Support")

        create_role_gestion = Role(role="Gestion")

        create_admin = User(
            first_name="admin",
            last_name="admin",
            email="admin@email.com",
            password="admin",
            is_superuser=True,
            date_created=datetime.now(),
            last_login=datetime.now(),
            role_id=3,
        )

        create_user = User(
            first_name="Jean",
            last_name="Lambda",
            email="jl@email.com",
            password="S3cret!",
            is_superuser=False,
            date_created=datetime.now(),
            last_login=datetime.now(),
            role_id=1,
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
        any_key = input("Press any key to close app...")

        # close session
        session.close()

        # clear console
        Utils().clear_console()

        # delete database
        os.remove(database_path)

    def start_cli_prod_mod():
        """
        Prod mode with persistent data
        """
        # call sentry
        call_centry()

        # Supprimer les avertissements SAWarning
        warnings.filterwarnings("ignore", category=sa_exc.SAWarning)

        # create session
        session = Session()

        # create database if not exists
        Base.metadata.create_all(
            engine,
            tables=[
                Role.__table__,
                User.__table__,
                Customer.__table__,
                Contract.__table__,
                Event.__table__,
            ],
        )

        # Vérifier si les rôles existent déjà dans la base de données
        if (
            not session.query(Role)
            .filter(Role.role.in_(["Sale", "Support", "Gestion"]))
            .first()
        ):
            create_role_sale = Role(role="Sale")

            create_role_support = Role(role="Support")

            create_role_gestion = Role(role="Gestion")

            session.add_all(
                [create_role_sale, create_role_support, create_role_gestion]
            )
            session.commit()

        # Vérifier si l'administrateur existe déjà dans la base de données
        if not session.query(User).filter(User.is_superuser is True).first():
            create_admin = User(
                first_name="admin",
                last_name="admin",
                email="admin@email.com",
                password="admin",
                is_superuser=True,
                date_created=datetime.now(),
                last_login=datetime.now(),
                role_id=3,
            )

            session.add(create_admin)

        router = Console()
        router.routing()

        # close session
        session.close()

        # clear console
        Utils().clear_console()

    def start_cli_soutenance_mod():
        """
        Start the application
        """
        # call sentry
        call_centry()

        # Supprimer les avertissements SAWarning
        warnings.filterwarnings("ignore", category=sa_exc.SAWarning)

        database_path = "database/database.db"

        if os.path.isfile(database_path):
            os.remove(database_path)

        # create session
        session = Session()

        # create database if not exists
        Base.metadata.create_all(
            engine,
            tables=[
                Role.__table__,
                User.__table__,
                Customer.__table__,
                Contract.__table__,
                Event.__table__,
            ],
        )

        # Vérifier si les rôles existent déjà dans la base de données
        if (
            not session.query(Role)
            .filter(Role.role.in_(["Sale", "Support", "Gestion"]))
            .first()
        ):
            create_role_sale = Role(role="Sale")

            create_role_support = Role(role="Support")

            create_role_gestion = Role(role="Gestion")

            session.add_all(
                [create_role_sale, create_role_support, create_role_gestion]
            )
            session.commit()

        # Vérifier si l'administrateur existe déjà dans la base de données
        if not session.query(User).filter(User.is_superuser is True).first():
            create_admin = User(
                first_name="admin",
                last_name="admin",
                email="admin@email.com",
                password="admin",
                is_superuser=True,
                date_created=datetime.now(),
                last_login=datetime.now(),
                role_id=3,
            )

            session.add(create_admin)

            create_saler = User(
                first_name="saler",
                last_name="saler",
                email="saler@email.com",
                password="saler",
                is_superuser=False,
                date_created=datetime.now(),
                last_login=datetime.now(),
                role_id=1,
            )

            session.add(create_saler)

            create_support = User(
                first_name="support",
                last_name="support",
                email="support@email.com",
                password="support",
                is_superuser=False,
                date_created=datetime.now(),
                last_login=datetime.now(),
                role_id=2,
            )

            session.add(create_support)

            create_gestion = User(
                first_name="gestion",
                last_name="gestion",
                email="gestion@email.com",
                password="gestion",
                is_superuser=False,
                date_created=datetime.now(),
                last_login=datetime.now(),
                role_id=3,
            )

            session.add(create_gestion)

            session.commit()

        router = Console()
        router.routing()

        # close session
        session.close()

        # clear console
        Utils().clear_console()

        # delete database
        os.remove(database_path)
