class Generic_Errors:
    def __init__(self):
        pass

    @staticmethod
    def login_error():
        """
        Display error message if the id is not in the database
        """
        return print("/_!_\\ L'email ou le mot de passe est incorrect /_!_\\")

    @staticmethod
    def unknown_role():
        """
        Display error message if the user role is unknown
        """
        return print("/_!_\\ Le role de l'utilisateur est inconnu /_!_\\")

    @staticmethod
    def wrong_input():
        """
        Display error message if the user input is wrong
        """
        return print("/_!_\\ Votre choix est incorrect /_!_\\")
