from flask_seeder import Seeder, generator, Faker
from ..contracts_model import Contract
from config import Session
from datetime import datetime
import random


class ContractSeeder(Seeder):
    def run(self):
        session = Session()

        faker = Faker(
            cls=Contract,
            init={
                "id": generator.Sequence(),
                "customer_id": generator.Integer(start=1, end=5),
                "sale_contact_id": generator.Integer(start=1, end=5),
                "amount": generator.Integer(start=1, end=500),
                "rest": generator.Integer(start=1, end=400),
                "creation_date": datetime.utcnow(),
                "status": generator.Integer(start=0, end=1),
            },
        )

        for contract in faker.create(5):
            print("Adding contract: %s" % contract)
            session.add(contract)
            session.commit()
