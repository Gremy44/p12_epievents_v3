from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base
from argon2 import PasswordHasher

Base = declarative_base()
ph = PasswordHasher()

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    role = Column(String(50))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    date_created = Column(DateTime)
    last_login = Column(DateTime)
    role_id = Column(Integer, ForeignKey('role.id'), default=1)

    role = relationship(Role)

    @validates('password')
    def validate_password(self, key, password):
        hashed_password = ph.hash(password)
        return hashed_password
    
    def verify_password(self, password):
        """
        Vérifie si le mot de passe fourni correspond au mot de passe stocké dans le modèle.

        Args:
        - password (str): Mot de passe fourni par l'utilisateur.

        Returns:
        - bool: True si le mot de passe est correct, False sinon.
        """
        try:
            ph.verify(self.password, password)
            return True
        except Exception:
            return False

