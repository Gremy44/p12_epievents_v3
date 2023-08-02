from views.login_view import Login_view
from models.users_model import User
from config import Session
from datetime import datetime


class Login_Controller:
    def __init__(self):
        pass

    def login(self):
        """
        Call the login view
        """
        view = Login_view()
        
        # store user id
        self.id = view.login()

        # logout
        if self.id is None:
            return

        return (self.id_validation(), self.logged_user())

    def id_validation(self):
        """
        Check if the id is in the database
        Check if the password is correct

        Returns:
        bool: True if the id is in the database
        """
        # retrieve session
        session = Session()

        user = session.query(User).filter_by(email=self.id[0]).first()
        
        session.close()

        if user and user.verify_password(self.id[1]):
            return True
        else:
            return False

    def update_last_login(self, user):
        session = Session()

        user.last_login = datetime.now()

        session.commit()
        
        session.close()

    def logged_user(self):
        """
        Return the user object
        """
        # retrieve session
        session = Session()

        user = session.query(User).filter_by(email=self.id[0]).first()
        
        session.close()

        return user
