from utils.utils import Utils
from utils.validators import Validators


class User_View:
    def __init__(self):
        self.validator = Validators()

    def users_id_input(self, length_queryset):
        print("Entrer l'id de l'Utilisateur : ")
        id = self.validator.validator_menu_choice(1, length_queryset)
        return id

    def users_add_validate(self):
        print("L'utilisateur a bien été ajouté !")
        Utils().wait_user_input()

    def users_update_validate(self):
        print("L'utilisateur a bien été modifié !")
        Utils().wait_user_input()

    def users_delete_validate(self):
        print("L'utilisateur a bien été supprimé !")
        Utils().wait_user_input()

    def users_crud_action(self):
        print("----------------------------")
        print("1 - Détail d'un utilisateur")
        print("2 - Ajouter un utilisateur")
        print("3 - Modifier un utilisateur")
        print("4 - Supprimer un utilisateur")
        print("5 - Retour")
        print("----------------------------")

    def users_view_list(self, table_name, users, length_queryset):
        """
        View users

        Returns:
            tuple: choix:str, id_users:int
        """
        Utils().clear_console()

        print("----------------------------------------------------------")  # 58
        print(f"----------------------{table_name}-------------------------")  #
        print("----------------------------------------------------------")  # 58
        print("Nombre d'utilisateurs : ", length_queryset)

        for user in users:
            print(
                f"N°: {user.id}|Nom: {user.last_name}|Prenom: {user.first_name}|Role: {user.role.role}"
            )

        self.users_crud_action()

        choice = self.validator.validator_menu_choice(1, 5)

        return choice

    def users_view_detail(self, user):
        """
        View user details

        Args:
            user(user): user query
        """
        Utils().clear_console()
        print(f"ID : {user.id}")
        print(f"Nom : {user.last_name}")
        print(f"Prénom : {user.first_name}")
        print(f"Email : {user.email}")
        print(f"Actif : {user.is_active}")
        print(f"Date création : {user.date_created}")
        print(f"Dernière connexion : {user.last_login}")
        print(f"Role : {user.role.role}")
        print("----------------------------------------------------------")
        Utils().wait_user_input()

    def users_view_add(self):
        """
        View user add

        Args:
            table_name (str): table name
        """
        Utils().clear_console()

        print("----------------------------------------------------------")
        print("----------------  Nouvel utilisateur  --------------------")
        print("----------------------------------------------------------")

        last_name = self.validator.validator_simple_text("last_name", "- Nom : ", False)
        first_name = self.validator.validator_simple_text(
            "first_name", "- Prénom : ", False
        )
        email = self.validator.validator_email("email", "- Email : ", False)
        password = self.validator.validator_password(
            "password", "- Mot de passe : ", False
        )
        role_id = self.validator.validator_role(
            "role_id", "- Role (1-Vendeur|2-Support|3-Gestion): ", False
        )

        return {
            "last_name": last_name,
            "first_name": first_name,
            "email": email,
            "password": password,
            "role": role_id,
        }

    def users_view_update(self, user):
        """
        View user update

        Args:
            user(User): user object
        """

        Utils().clear_console()

        print("----------------------------------------------------------")
        print("---------------  Modifier l'utilisateur  -----------------")
        print("----------------------------------------------------------")
        print("----------  Laissez le champ vide si inchangé  -----------")
        print("----------------------------------------------------------")

        print(f"Nom : {user.last_name}")
        last_name = self.validator.validator_simple_text(
            "last_name", "- Modifier le Nom : ", True
        )
        print(f"Prénom : {user.first_name}")
        first_name = self.validator.validator_simple_text(
            "first_name", "- Modifier le Prénom : ", True
        )
        print(f"Email : {user.email}")
        email = self.validator.validator_email("email", "- Modifier l'email : ", True)
        print(f"Mot de passe :")
        password = self.validator.validator_password(
            "password", "- Modifier le Mot de passe : ", True
        )
        print(f"Role : {user.role.role}")
        role_id = self.validator.validator_role(
            "role_id", "- Modifier le Role (1-Vendeur|2-Support|3-Gestion): ", True
        )

        return {
            "last_name": last_name,
            "first_name": first_name,
            "email": email,
            "password": password,
            "role_id": role_id,
        }
