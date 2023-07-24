from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .users_model import User, Base
from .contracts_model import Contract
from .customers_model import Customer


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    location = Column(String(100))
    attendees = Column(String(255))
    notes = Column(String(255))
    client_id = Column(Integer, ForeignKey('customer.id'))
    contract_id = Column(Integer, ForeignKey('contract.id'))
    support_contact_id = Column(Integer, ForeignKey('user.id'))

    client = relationship(Customer, foreign_keys=[client_id])
    contract = relationship(Contract, foreign_keys=[contract_id])
    support_contact = relationship(User, foreign_keys=[support_contact_id])
