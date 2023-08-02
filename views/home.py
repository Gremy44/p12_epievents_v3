from views.generic_errors import Generic_Errors
from utils.validators import Validators
from utils.utils import Utils
from config import Session
import sys


class Home_view:
    def __init__(self, user):
        self.validator = Validators()
        self.user = user
        self.quit_message = (
            "Vous êtes déconnecté, appuyer sur une touche pour continuer..."
        )
        self.session = Session()

    def home(self):
        """
        Display the home view
        """
        Utils().clear_console()

        print("----------------------------------------------------------")  # 58
        print("----------------------    HOME   -------------------------")  #
        print("----------------------------------------------------------")  # 58

        if self.user.is_superuser is True:
            return self.menu_admin()

        elif self.user.is_superuser is False and self.user.role_id == 1:
            return self.menu_sale()

        elif self.user.is_superuser is False and self.user.role_id == 2:
            return self.menu_support()

        elif self.user.is_superuser is False and self.user.role_id == 3:
            return self.menu_gestion()

        else:
            Generic_Errors().unknown_role()

    def menu_admin(self):
        """
        Display the admin menu
        """

        print(
            f"ADMIN-{self.user.last_name} {self.user.first_name}"
        )
        print("1 - Gestion des Clients")
        print("2 - Gestion des Contrats")
        print("3 - Gestion des Evènements")
        print("4 - Gestion des Utilisateurs")
        print("5 - Logout")

        choice = self.validator.validator_home("response", "Votre choix : ", self.user)

        is_logged = True

        if choice == "5":
            Utils().clear_console()
            input(self.quit_message)
            self.session.close()
            is_logged = False

        return (choice, (1, 4), is_logged)

    def menu_sale(self):
        """
        Display the sale menu
        """
        print(
            f"SALE-{self.user.last_name} {self.user.first_name}"
        )
        print("1 - Gestion des Clients")
        print("2 - Gestion des Contrats")
        print("3 - Gestion des Evènements")
        print("4 - Logout")

        choice = self.validator.validator_home("response", "Votre choix : ", self.user)

        is_logged = True

        if choice == "4":
            Utils().clear_console()
            input(self.quit_message)
            self.session.close()
            is_logged = False

        return (choice, (1, 3), is_logged)

    def menu_support(self):
        """
        Display the support menu
        """
        print(
            f"SUPPORT-{self.user.last_name} {self.user.first_name}"
        )
        print("1 - Gestion des Clients")
        print("2 - Gestion des Contrats")
        print("3 - Gestion des Evènements")
        print("4 - Logout")

        choice = self.validator.validator_home("response", "Votre choix : ", self.user)

        is_logged = True

        if choice == "4":
            Utils().clear_console()
            input(self.quit_message)
            self.session.close()
            is_logged = False

        return (choice, (1, 3), is_logged)

    def menu_gestion(self):
        """
        Display the gestion menu
        """
        print(
            f"GESTION-{self.user.last_name} {self.user.first_name}"
        )
        print("1 - Gestion des Clients")
        print("2 - Gestion des Contrats")
        print("3 - Gestion des Evènements")
        print("4 - Gestion des Utilisateurs")
        print("5 - Logout")

        choice = self.validator.validator_home("response", "Votre choix : ", self.user)

        is_logged = True

        if choice == "5":
            Utils().clear_console()
            input(self.quit_message)
            self.session.close()
            is_logged = False

        return (choice, (1, 4), is_logged)
