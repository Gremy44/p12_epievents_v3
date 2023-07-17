from flask_seeder import Seeder, Faker, generator
from sqlalchemy.orm import sessionmaker
from config import engine
from models.users_model import User
import random
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()

# All seeders inherit from Seeder
class UserSeeder(Seeder):
  # run() will be called by Flask-Seeder
  def run(self):
    db = self.db
    # Create a new Faker and tell it how to create User objects
    faker = Faker(
      cls=User,
      init={
        "id": generator.Sequence(),
        "first_name": generator.Name(),
        "last_name": generator.Name(),
        "email": generator.Email(),
        "password": "S3cret!",
        "is_active": True,
        "is_superuser": False,
        "date_created": datetime.utcnow(),
        "last_login": datetime.utcnow(),
        "role_id": random.randint(1, 3)
      }
    )

    # Create 5 users
    for user in faker.create(5):
        print("Adding user: %s" % user)
        session.add(user)
        session.commit()