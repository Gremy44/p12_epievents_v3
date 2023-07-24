import os

from config import Session
from models.users_model import User
from models.customers_model import Customer
from models.contracts_model import Contract

class Utils:
    def __init__(self):
        pass
    
    def clear_console(self):
        '''
        Clear the console
        '''
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait_user_input(self):
        '''
        Wait for user input
        '''
        input("Appuyez sur une touche pour continuer...")
        
    def retrieve_saler(self):
        '''
        Return the saler
        
        Returns:
            query_set: user filter by role sale
        '''
        session = Session()
        
        salers = session.query(User).filter(User.role_id == 1).all()
        
        return salers
    
    def retrieve_support(self):
        '''
        Return the support
        
        Returns:
            query_set: user filter by role support
        '''
        session = Session()
        
        supports = session.query(User).filter(User.role_id == 2).all()
        
        return supports

    def retrieve_gestion(self):
        '''
        Return the gestion
        
        Returns:
            query_set: user filter by role gestion
        '''
        session = Session()
        
        gestion = session.query(User).filter(User.role_id == 3).all()
        
        return gestion
    
    def retrieve_client(self):
        '''
        Return the client
        
        Returns:
            a print of customers
        '''
        session = Session()
        
        clients = session.query(Customer).all()
        
        for client in clients:
            print(f"ID: {client.id}||Nom: {client.complet_name}|| Compagnie: {client.company_name}")
            
    def retrieve_contract(self):
        '''
        Return the contract
        '''
        session = Session()
        
        contracts = session.query(Contract).all()
        
        for contract in contracts:
            customer_name = contract.customer.complet_name if contract.customer else "N/A"
            company_name = contract.customer.company_name if contract.customer else "N/A"
            print(f"ID: {contract.id}||Client associé: {customer_name}|| Compagnie: {company_name}")
        

    def print_queryset(self, queryset):
        '''
        Print the queryset
        print(f"ID: {s.id}||Nom: {s.first_name} {s.last_name}")
        
        Args:
            queryset (query_set): query set
        '''
        for s in queryset:
            print(f"ID: {s.id}||Nom: {s.first_name} {s.last_name}")
            