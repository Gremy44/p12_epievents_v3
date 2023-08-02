from datetime import datetime

import sentry_sdk

from config import Session
from views.contracts_view import Contracts_View
from models.contracts_model import Contract
from models.customers_model import Customer
from permissions.permissions import Permissions
from sentry_config import call_centry


class Contracts_Controller:
    def __init__(self, user):
        self.my_view = Contracts_View()
        self.user = user
        call_centry()

    def contracts_menu(self):
        """
        Call contract view to display all contracts
        """
        table_name = "Contracts"

        session = Session()
        contracts = session.query(Contract).all()

        customers = session.query(Customer).all()

        choix = self.my_view.contracts_view_list(
            table_name, contracts, contracts.__len__()
        )

        try:
            match choix[0]:
                case "1":
                    # if no contracts
                    if contracts.__len__() == 0:
                        input("Aucun contrat à afficher, appuyer sur une touche pour continuer")
                        return

                    contract_id = self.my_view.contracts_id_input(
                        contracts.__len__()
                        )
                    self.contracts_detail(contract_id)
                case "2":
                    if customers.__len__() == 0:
                        input("Il n'y a pas de clients pour créer un contrat,"
                              "appuyer sur une touche pour continuer"
                              )
                        return

                    self.contracts_add()
                case "3":
                    if contracts.__len__() == 0:
                        input("Aucun contrat à afficher, appuyer sur une touche pour continuer")
                        return

                    contract_id = self.my_view.contracts_id_input(
                        contracts.__len__()
                        )
                    self.contracts_update(contract_id)
                case "4":
                    if contracts.__len__() == 0:
                        input("Aucun contrat à afficher, appuyer sur une touche pour continuer")
                        return

                    contract_id = self.my_view.contracts_id_input(
                        contracts.__len__()
                        )
                    self.contracts_delete(contract_id)
        except IndexError:
            return

    def contracts_detail(self, contract_id):
        """
        Show contract details

        args:
            user (User): User object representing the current user
            contract_id (int): contract id
        """
        session = Session()

        contract = session.query(Contract).filter(
            Contract.id == contract_id).first()

        self.my_view.contracts_view_detail(contract)

    @Permissions.gestion_required
    def contracts_add(self):
        """
        Call contracts view to add a contract
        """
        session = Session()

        form = self.my_view.contracts_view_add()

        create_contract = Contract(
            customer_id=form["customer_id"],
            sale_contact_id=form["sale_contact_id"],
            amount=form["amount"],
            rest=form["rest"],
            status=form["status"],
        )

        session.add(create_contract)
        session.commit()

        self.my_view.contracts_add_validate()

    @Permissions.sale_or_gestion_required
    def contracts_update(self, contract_id):
        session = Session()

        contract = session.query(Contract).filter(
            Contract.id == contract_id).first()

        form = self.my_view.contracts_view_update(contract)

        if form["customer_id"] != "":
            contract.customer_id = form["customer_id"]
        if form["sale_contact_id"] != "":
            contract.sale_contact_id = form["sale_contact_id"]
        if form["amount"] != "":
            contract.amount = form["amount"]
        if form["rest"] != "":
            contract.rest = form["rest"]
        if form["status"] != "":
            if form["status"] == "1":
                contract.status = True

                # send contract info to sentry
                sentry_sdk.capture_message(
                    f"Contrat Signé : {contract.customer_id}|\
                        {contract.sale_contact_id}|{contract.amount}|\
                        {contract.rest}|{contract.status} at {datetime.now()}",
                    level="info",
                )
            else:
                contract.status = False

        session.commit()

        self.my_view.contracts_update_validate()

    @Permissions.admin_required
    def contracts_delete(self, contract_id):
        session = Session()

        contract = session.query(Contract).filter(
            Contract.id == contract_id).first()

        session.delete(contract)
        session.commit()

        self.my_view.contracts_delete_validate()
