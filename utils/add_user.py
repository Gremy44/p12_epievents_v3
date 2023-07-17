from models.users_model import User, Role, Base
from sqlalchemy.orm import sessionmaker
from config import engine
from datetime import datetime
from sqlalchemy.orm import validates
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Créez une session
Session = sessionmaker(bind=engine)
session = Session()

ph = PasswordHasher()


class Add_user:
    
    def __init__(self, fn:str, ln:str, pw:str):
        self.fn = fn
        self.ln = ln
        self.pw = pw

    def create_user(self):
        user = User(
            first_name= f'{self.fn}',
            last_name= f'{self.ln}',
            email=f'{self.fn}.{self.ln}@example.com',
            password=self.password_hash(self.pw),
            is_active=True,
            date_created=datetime.now(),
            last_login=datetime.now(),
            role_id=1  # Remplacez 1 par l'ID du rôle approprié
        )

        session.add(user)
        session.commit()

    def password_hash(self, pw):
        return ph.hash(pw)
