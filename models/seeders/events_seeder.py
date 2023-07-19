from flask_seeder import Seeder, generator, Faker
from models.events_model import Event
from config import Session
from datetime import datetime


class EventSeeder(Seeder):
    
    def run(self):
        
        session = Session()
        
        faker = Faker(
            cls=Event,
            init={
                "id": generator.Sequence(),
                "event_name":"test "+str(generator.Sequence()),
                "date_start":datetime.utcnow(),
                "date_end":datetime.utcnow(),
                "location":generator.Name(),
                "attendees":generator.Integer(start=1, end=100),
                "notes":"note "+str(generator.Sequence()),
                "client_id":generator.Integer(start=1, end=5),
                "contract_id":generator.Integer(start=1, end=5),
                "support_contact_id":generator.Integer(start=1, end=3),
            }
        )
        
        for event in faker.create(5):
            print("Adding event: %s" % event)
            session.add(event)
            session.commit()
