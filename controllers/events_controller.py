from datetime import datetime

from config import Session
from views.events_view import Events_View
from models.events_model import Event

class Events_Controller:
    
    def __init__(self):
        self.my_view = Events_View()
    
    def events_menu(self):
        """_summary_
        Call custormers view to display all events
        """
        table_name = "Clients"
        
        
        session = Session()
        events = session.query(Event).all()
        
        choix = self.my_view.events_view_list(table_name, events)
        
        try:
            match choix[0]:
                case "1":
                    event_id = self.my_view.events_id_input()
                    self.events_detail(event_id)
                case "2":
                    self.events_add()
                case "3":
                    event_id = self.my_view.events_id_input()
                    self.events_update(event_id)
                case "4":
                    event_id = self.my_view.events_id_input()
                    self.events_delete(event_id)
        except IndexError:
            return
    
    def events_detail(self, event_id):
        """_summary_
        Show event details
        
        args:
            event_id (int): event id
        """
        session = Session()
        
        event = session.query(Event).filter(Event.id == event_id).first()
        
        self.my_view.events_view_detail(event)
    
    def events_add(self):
        """_summary_
        Call custormers view to add a event
        
        Returns:
            _type_: _description_
        """
        session = Session()
        
        form = self.my_view.events_view_add()
        
        # format the user input date to valide datetime for db
        form['date_start'] = datetime.strptime(form['date_start'], '%d/%m/%Y')
        form['date_end'] = datetime.strptime(form['date_end'], '%d/%m/%Y')
        
        create_event = Event(
            name=form['name'],
            date_start=form['date_start'],
            date_end=form['date_end'],
            location=form['location'],
            attendees=form['attendees'],
            notes=form['notes'],
            client_id=form['client_id'],
            contract_id=form['contract_id'],
            support_contact_id=form['support_contact_id'],
        )
        
        session.add(create_event)
        session.commit()
        
        self.my_view.events_add_validate()
    
    def events_update(self, event_id):
        
        session = Session()
        
        event = session.query(Event).filter(Event.id == event_id).first()
        
        form = self.my_view.events_view_update(event)
        
        if form['name'] != "":
            event.name = form['name']
        if form['date_start'] != "":
            event.date_start = form['date_start']
        if form['date_end'] != "":
            event.date_end = form['date_end']
        if form['location'] != "":
            event.location = form['location']
        if form['attendees'] != "":
            event.attendees = form['attendees']
        if form['notes'] != "":
            event.notes = form['notes']
        if form['client_id'] != "":
            event.client_id = form['client_id']
        if form['contract_id'] != "":
            event.contract_id = form['contract_id']
        if form['support_contact_id'] != "":
            event.support_contact_id = form['support_contact_id']
        
        session.commit()
        
        self.my_view.events_update_validate()
    
    def events_delete(self, event_id):
        
        session = Session()
        
        event = session.query(Event).filter(Event.id == event_id).first()
        
        session.delete(event)
        session.commit()
        
        self.my_view.events_delete_validate()
