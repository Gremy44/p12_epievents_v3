from utils.utils import Utils
from utils.validators import Validators


class Contracts_View:
    def __init__(self):
        self.validator = Validators()

    def contracts_id_input(self, length_queryset):
        print("Entrer l'id du Contrat : ")
        id = self.validator.validator_menu_choice(1, length_queryset)
        return id

    def contracts_add_validate(self):
        print("Le Contrat a bien été ajouté !")
        Utils().wait_user_input()

    def contracts_update_validate(self):
        print("Le Contrat a bien été modifié !")
        Utils().wait_user_input()

    def contracts_delete_validate(self):
        print("Le Contrat a bien été supprimé !")
        Utils().wait_user_input()

    def contracts_crud_action(self):
        print("----------------------------")
        print("1 - Détail du Contrat")
        print("2 - Ajouter un Contrat")
        print("3 - Modifier un Contrat")
        print("4 - Supprimer un Contat")
        print("5 - Retour")
        print("----------------------------")

    def contracts_view_list(self, table_name, contracts, length_queryset):
        """
        View contracts

        Returns:
            tuple: choix:str, id_contract:int
        """
        Utils().clear_console()

        print("----------------------------------------------------------")  # 58
        print(f"----------------------{table_name}-------------------------")  #
        print("----------------------------------------------------------")  # 58
        print("Nombre de contrats: ", length_queryset)

        for contract in contracts:
            print(
                f"ID: {contract.id} | Client: {contract.customer.complet_name} |"
                f"Company: {contract.customer.company_name} |"
                f"Montant du contrat: {contract.amount} |"
                f"Rest à payer: {contract.rest} | Status: {contract.status}"
            )

        self.contracts_crud_action()

        choice = self.validator.validator_menu_choice(1, 5)

        return choice

    def contracts_view_detail(self, contract):
        """
        View contract details

        Args:
            contract (Contract): contract object
        """
        Utils().clear_console()

        print(f"ID : {contract.id}")
        print(f"Nom du Client : {contract.customer.complet_name}")
        print(f"Entreprise du Client : {contract.customer.company_name}")
        print(
            f"Contact vendeur : {contract.sale_contact.first_name} {contract.sale_contact.last_name}"
        )
        print(f"Montant du contrat : {contract.amount} €")
        print(f"Reste à payer : {contract.rest}")
        print(f"Status du contrat : {contract.status}")
        print("----------------------------------------------------------")
        Utils().wait_user_input()

    def contracts_view_add(self):
        """
        View contract add

        Args:
            table_name (str): table name
        """
        Utils().clear_console()

        print("----------------------------------------------------------")  # 58
        print("-------------------  NOUVEAU CONTRAT  --------------------")  #
        print("----------------------------------------------------------")  # 58

        print("Client a associer au contrat :")
        print("-- Clients présents dans la base de données --")
        clients = Utils().retrieve_client()
        # customer_id = input("- ID du client: ")
        customer_id = self.validator.validator_id("customer_id", "- ID du client: ", False)
        customer_id = self.validator.check_interval(customer_id, 1, clients.__len__())
        customer_id = customer_id[1]

        print("Vendeur à associer au contrat :")
        print("-- Vendeurs présents dans la base de données --")
        sale = Utils().retrieve_saler()
        Utils().print_queryset(sale)
        # sale_contact_id = input("- ID du contact vendeur: ")
        sale_contact_id = self.validator.validator_id("sale_contact_id", "- ID du contact vendeur: ", False)

        # amount = input("- Montant du contrat ")
        amount = self.validator.validator_phone("amount", "- Montant du contrat: ", False)
        rest = amount
        status = False

        return {
            "customer_id": customer_id,
            "sale_contact_id": sale_contact_id,
            "amount": amount,
            "rest": rest,
            "status": status,
        }

    def contracts_view_update(self, contract):
        """
        View contract update

        Args:
            contract (Contract): contract object
        """

        Utils().clear_console()

        print("----------------------------------------------------------")
        print("----------------  Modifier le CONTRACT  -------------------")
        print("----------------------------------------------------------")
        print("----------  Laissez le champ vide si inchangé  -----------")
        print("----------------------------------------------------------")

        print(f"ID du client: {contract.customer_id}")
        print("-- Clients présents dans la base de données --")
        clients = Utils().retrieve_client()
        # customer_id = input("- Modifier l'ID : ")
        customer_id = self.validator.validator_id("customer_id", "- Modifier l'ID : ", True)
        self.validator.check_interval(customer_id, 1, clients.__len__())

        print(f"ID contact vendeur : {contract.sale_contact_id}")
        print("-- Vendeurs présents dans la base de données --")
        sale = Utils().retrieve_saler()
        Utils().print_queryset(sale)
        # sale_contact_id = input("- Modifier la Date de Début : ")
        sale_contact_id = self.validator.validator_id(
            "sale_contact_id", "- Modifier Contact vendeur : ", True)

        print(f"Montant du contrat : {contract.amount}")
        # amount = input("- Modifier le montant : ")
        amount = self.validator.validator_phone("amount", "- Modifier le montant : ", True)

        print(f"Reste à régler : {contract.rest}")
        # rest = input("- Modifier le reste : ")
        rest = self.validator.validator_phone("rest", "- Modifier le reste : ", True)

        print(f"Status du contrat : ID: {contract.status}")
        # status = input("- Modifier le status du contrat (1 ou 0): ")
        status = self.validator.validator_id("status", "- Modifier le status du contrat (1 ou 0): ", True)
        self.validator.check_interval(status, 0, 1)

        return {
            "customer_id": customer_id,
            "sale_contact_id": sale_contact_id,
            "amount": amount,
            "rest": rest,
            "status": status,
        }
