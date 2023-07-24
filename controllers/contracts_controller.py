from datetime import datetime

from config import Session
from views.contracts_view import Contracts_View
from models.contracts_model import Contract

class Contracts_Controller:
    
    def __init__(self):
        self.my_view = Contracts_View()
    
    def contracts_menu(self):
        """
        Call contract view to display all contracts
        """
        table_name = "Contracts"
        
        
        session = Session()
        contracts = session.query(Contract).all()
        
        choix = self.my_view.contracts_view_list(table_name, contracts)
        
        try:
            match choix[0]:
                case "1":
                    contract_id = self.my_view.contracts_id_input()
                    self.contracts_detail(contract_id)
                case "2":
                    self.contracts_add()
                case "3":
                    contract_id = self.my_view.contracts_id_input()
                    self.contracts_update(contract_id)
                case "4":
                    contract_id = self.my_view.contracts_id_input()
                    self.contracts_delete(contract_id)
        except IndexError:
            return

    def contracts_detail(self, contract_id):
        """
        Show contract details
        
        args:
            contract_id (int): contract id
        """
        session = Session()
        
        contract = session.query(Contract).filter(Contract.id == contract_id).first()
        
        self.my_view.contracts_view_detail(contract)
        
    def contracts_add(self):
        """
        Call contracts view to add a contract
        """
        session = Session()
        
        form = self.my_view.contracts_view_add()
        
        create_contract = Contract(
            customer_id=form['customer_id'],
            sale_contact_id=form['sale_contact_id'],
            amount=form['amount'],
            rest=form['rest'],
            status=form['status'],
        )
        
        session.add(create_contract)
        session.commit()
        
        self.my_view.contracts_add_validate()
        
    def contracts_update(self, contract_id):
        
        session = Session()
        
        contract = session.query(Contract).filter(Contract.id == contract_id).first()
        
        form = self.my_view.contracts_view_update(contract)
        
        if form['customer_id'] != "":
            contract.customer_id = form['customer_id']
        if form['sale_contact_id'] != "":
            contract.sale_contact_id = form['sale_contact_id']
        if form['amount'] != "":
            contract.amount = form['amount']
        if form['rest'] != "":
            contract.rest = form['rest']
        if form['status'] != "":
            contract.status = form['status']
        
        session.commit()
        
        self.my_view.contracts_update_validate()
        
    def contracts_delete(self, contract_id):
        
        session = Session()
        
        contract = session.query(Contract).filter(Contract.id == contract_id).first()
        
        session.delete(contract)
        session.commit()
        
        self.my_view.contracts_delete_validate()