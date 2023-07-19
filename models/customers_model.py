from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .users_model import User
from .users_model import Base

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    complet_name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    company_name = Column(String(100))
    creation_date = Column(DateTime, default=datetime.utcnow)
    date_update = Column(DateTime, onupdate=datetime.utcnow)
    sale_contact_id = Column(Integer, ForeignKey('user.id'))

    sale_contact = relationship(User)
