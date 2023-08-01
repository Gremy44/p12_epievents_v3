from utils.utils import Utils
from utils.validators import Validators


class Customers_View:
    def __init__(self) -> None:
        self.validator = Validators()

    def customers_id_input(self, length_queryset):
        print("Entrer l'id du Client : ")
        id = self.validator.validator_menu_choice(1, length_queryset)
        return id

    def customers_add_validate(self):
        print("Le client a bien été ajouté !")
        Utils().wait_user_input()

    def customers_update_validate(self):
        print("Le client a bien été modifié !")
        Utils().wait_user_input()

    def customers_delete_validate(self):
        print("Le client a bien été supprimé !")
        Utils().wait_user_input()

    def customers_crud_action(self):
        print("----------------------------")
        print("1 - Détail d'un Client")
        print("2 - Ajouter un Client")
        print("3 - Modifier un Client")
        print("4 - Supprimer un Client")
        print("5 - Retour")
        print("----------------------------")

    def customers_view_list(self, table_name, customers, length_queryset):
        """
        View customers

        Returns:
            tuple: choix:str, id_customer:int
        """
        Utils().clear_console()

        print("----------------------------------------------------------")  # 58
        print(f"----------------------{table_name}-------------------------")  #
        print("----------------------------------------------------------")  # 58
        print("Nombre de clients : ", length_queryset)

        for customer in customers:
            print(
                f"N°: {customer.id}|Nom: {customer.complet_name}|"
                f"Email: {customer.email}|Tel: {customer.phone}|"
                f"Compagnie: {customer.company_name}|"
                f"Contacte vendeur: {customer.sale_contact.first_name}"
            )

        self.customers_crud_action()

        choice = self.validator.validator_menu_choice(1, 5)

        return choice

    def customers_view_detail(self, customer):
        """
        View customer details

        Args:
            customer (Customer): customer object
        """
        Utils().clear_console()

        print(f"Nom complet : {customer.complet_name}")
        print(f"Email : {customer.email}")
        print(f"Téléphone : {customer.phone}")
        print(f"Compagnie : {customer.company_name}")
        print(f"Date de création : {customer.creation_date}")
        print(f"Dernière modification : {customer.date_update}")
        print(
            f"Contacte vendeur : {customer.sale_contact.first_name} {customer.sale_contact.last_name}"
        )
        print("----------------------------------------------------------")
        Utils().wait_user_input()

    def customers_view_add(self):
        """
        View customer add

        Args:
            table_name (str): table name
        """
        Utils().clear_console()

        print("----------------------------------------------------------")  # 58
        print("------------------  Nouveau Client  ----------------------")  #
        print("----------------------------------------------------------")  # 58

        # complet_name = input("- Nom complet : ")
        complet_name = self.validator.validator_simple_text(
            "complet_name", "- Nom complet : ", False)
        # email = input("- Email : ")
        email = self.validator.validator_email("email", "- Email : ", False)
        # phone = input("- Téléphone : ")
        phone = self.validator.validator_phone("phone", "- Téléphone : ", False)
        # company_name = input("- Compagnie : ")
        company_name = self.validator.validator_simple_text(
            "company_name", "- Compagnie : ", False)

        return {
            "complet_name": complet_name,
            "email": email,
            "phone": phone,
            "company_name": company_name,
        }

    def customers_view_update(self, customer):
        """
        View customer update

        Args:
            customer (Customer): customer object
        """

        Utils().clear_console()

        print("----------------------------------------------------------")
        print("------------------  Modifier Client  ---------------------")
        print("----------------------------------------------------------")
        print("----------  Laissez le champ vide si inchangé  -----------")
        print("----------------------------------------------------------")

        print(f"Nom complet : {customer.complet_name}")
        complet_name = input("- Modifier Nom complet : ")
        print(f"Email : {customer.email}")
        email = input("- Modifier Email : ")
        print(f"Téléphone : {customer.phone}")
        phone = input("- Modifier Téléphone : ")
        print(f"Compagnie : {customer.company_name}")
        company_name = input("- Modifier Compagnie : ")
        print(
            f"Contacte de vente : ID: {customer.sale_contact.id} \
                || Nom: {customer.sale_contact.first_name} {customer.sale_contact.last_name}"
        )

        my_saler = Utils().retrieve_saler()
        Utils().print_queryset(my_saler)

        sale_contact_id = input("- Modifier Contact vendeur (ID): ")

        return {
            "complet_name": complet_name,
            "email": email,
            "phone": phone,
            "company_name": company_name,
            "sale_contact_id": sale_contact_id,
        }
