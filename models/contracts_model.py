from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .customers_model import Customer
from .users_model import User, Base


class Contract(Base):
    __tablename__ = "contract"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    sale_contact_id = Column(Integer, ForeignKey("user.id"))
    amount = Column(Numeric(precision=10, scale=2, asdecimal=True))
    rest = Column(Numeric(precision=10, scale=2, asdecimal=True))
    creation_date = Column(DateTime, default=datetime.utcnow)
    status = Column(Boolean, default=False)

    customer = relationship(Customer)
    sale_contact = relationship(User)
