from models.users_model import Base, User
from sqlalchemy.orm import sessionmaker
from config import engine
import datetime
from datetime import datetime

from views.login_view import Login_view

def start_cli():
    '''
    function call in main.py to start the cli
    '''

    login = Login_view()
    login.login()
