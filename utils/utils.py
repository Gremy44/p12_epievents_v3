import os

from config import Session
from models.users_model import User

class Utils:
    def __init__(self):
        pass
    
    def clear_console(self):
        '''
        Clear the console
        '''
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def user_role(self):
        '''
        Return the user role
        '''
        session = Session()
        
        user = session.query(User).filter_by(role=self.id[0]).first()
        
        return user.is_superuser
    
    def wait_user_input(self):
        '''
        Wait for user input
        '''
        input("Appuyez sur une touche pour continuer...")
