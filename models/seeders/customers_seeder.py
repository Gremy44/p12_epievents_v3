from flask_seeder import Seeder, generator, Faker
from ..customers_model import Customer
from config import Session
from datetime import datetime
import random

class CustomerSeeder(Seeder):
    
    def run(self):
        
        session = Session()
        
        faker = Faker(
            cls=Customer,
            init={
                "id": generator.Sequence(),
                "complet_name": generator.Name(),
                "email": generator.Email(),
                "phone": "0606060606",
                "company_name": generator.Name(),
                "creation_date": datetime.utcnow(),
                "date_update": datetime.utcnow(),
                "sale_contact_id": generator.Integer(start=1, end=3),
            }
        )
        
        for customer in faker.create(5):
            print("Adding customer: %s" % customer)
            session.add(customer)
            session.commit()

    