from datetime import datetime

from config import Session
from views.users_view import User_View
from models.users_model import User

from permissions.permissions import Permissions

from sentry_config import call_centry
import sentry_sdk


class Users_Controller:
    def __init__(self, user):
        self.my_view = User_View()
        self.user = user
        call_centry()

    @Permissions.gestion_required
    def users_menu(self):
        """_summary_
        Call custormers view to display all customers

        Returns:
            _type_: _value_
        """
        table_name = "Utilisateurs"

        session = Session()
        users = session.query(User).all()

        choix = self.my_view.users_view_list(
            table_name, users, users.__len__())

        try:
            match choix:
                case "1":
                    if users.__len__() == 0:
                        input("Aucun utilisateur à afficher, appuyer sur une touche pour continuer")
                        return

                    user_id = self.my_view.users_id_input(users.__len__())
                    self.users_detail(user_id)
                case "2":
                    self.users_add()
                case "3":
                    if users.__len__() == 0:
                        input("Aucun utilisateur à afficher, appuyer sur une touche pour continuer")
                        return

                    user_id = self.my_view.users_id_input(users.__len__())
                    self.users_update(user_id)
                case "4":
                    if users.__len__() == 0:
                        input("Aucun utilisateur à afficher, appuyer sur une touche pour continuer")
                        return

                    user_id = self.my_view.users_id_input(users.__len__())
                    self.users_delete(user_id)
        except IndexError:
            return

    @Permissions.gestion_required
    def users_detail(self, user_id):
        """_summary_
        Show user details

        args:
            user_id (int): user id
        """
        session = Session()

        user = session.query(User).filter(User.id == user_id).first()

        self.my_view.users_view_detail(user)

    @Permissions.gestion_required
    def users_add(self):
        """_summary_
        Call users view to add a user

        Returns:
            _type_: _description_
        """
        session = Session()

        form = self.my_view.users_view_add()

        create_user = User(
            last_name=form["last_name"],
            first_name=form["first_name"],
            email=form["email"],
            password=form["password"],
            date_created=datetime.now(),
            last_login=datetime.now(),
            role_id=form["role"],
        )

        session.add(create_user)
        session.commit()

        # send add info to sentry
        sentry_sdk.capture_message(
            f"User Create : {create_user.last_name}|\
                {create_user.first_name}|{create_user.email}|\
                {create_user.role_id} at {datetime.now()}",
            level="info",
        )

        self.my_view.users_add_validate()

    @Permissions.gestion_required
    def users_update(self, user_id):
        session = Session()

        user = session.query(User).filter(User.id == user_id).first()

        form = self.my_view.users_view_update(user)

        if form["last_name"] != "":
            user.last_name = form["last_name"]
        if form["first_name"] != "":
            user.first_name = form["first_name"]
        if form["email"] != "":
            user.email = form["email"]
        if form["password"] != "":
            user.password = form["password"]
        if form["role_id"] != "":
            user.role_id = form["role_id"]

        session.commit()

        # send update info to sentry
        sentry_sdk.capture_message(
            f"User Update : {user.last_name}|{user.first_name}|\
                {user.email}|{user.role_id} at {datetime.now()}",
            level="info",
        )

        self.my_view.users_update_validate()

    @Permissions.admin_required
    def users_delete(self, user_id):
        session = Session()

        user = session.query(User).filter(User.id == user_id).first()

        session.delete(user)
        session.commit()

        self.my_view.users_delete_validate()
