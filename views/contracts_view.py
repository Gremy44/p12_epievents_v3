from utils.utils import Utils
from views.generic_errors import Generic_Errors

class Contracts_View:
    def __init__(self):
        pass
    
    def contracts_id_input(self):
        return input("Entrer l'id du 'Contrat : ")
    
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
        print('----------------------------')
        print("1 - Détail du Contrat")
        print('2 - Ajouter un Contrat')
        print('3 - Modifier un Contrat')
        print('4 - Supprimer un Contat')
        print('5 - Retour')
        print('----------------------------')
        
    def contracts_view_list(self, table_name, contracts):
        '''
        View contracts
        
        Returns:
            tuple: choix:str, id_contract:int
        '''
        Utils().clear_console()
        
        print("----------------------------------------------------------") # 58
        print(f"----------------------{table_name}-------------------------") # 
        print("----------------------------------------------------------") # 58
        
        for contract in contracts:
            print(f"ID: {contract.id} | Client: {contract.customer.complet_name} | Company: {contract.customer.company_name} | Montant du contrat: {contract.amount} | Rest à payer: {contract.rest} | Status: {contract.status}")

    
        self.contracts_crud_action()
                
        return input("Votre choix : ")
    
    def contracts_view_detail(self, contract):
        '''
        View contract details
        
        Args:
            contract (Contract): contract object
        '''
        Utils().clear_console()
        
        print(f'ID : {contract.id}')
        print(f"Nom du Client : {contract.customer.complet_name}")
        print(f'Entreprise du Client : {contract.customer.company_name}')
        print(f'Contact vendeur : {contract.sale_contact.first_name} {contract.sale_contact.last_name}')
        print(f'Montant du contrat : {contract.amount} €')
        print(f'Reste à payer : {contract.rest}')
        print(f'Status du contrat : {contract.status}')
        print("----------------------------------------------------------")
        Utils().wait_user_input()
        
    def contracts_view_add(self):
        '''
        View contract add
        
        Args:
            table_name (str): table name
        '''
        Utils().clear_console()
        
        print("----------------------------------------------------------") # 58
        print("-------------------  NOUVEAU CONTRAT  --------------------") # 
        print("----------------------------------------------------------") # 58
        
        print("Client a associer au contrat :")
        print("-- Clients présents dans la base de données --")
        Utils().retrieve_client()
        customer_id = input("- ID du client: ")
        
        print("Vendeur à associer au contrat :")
        print("-- Vendeurs présents dans la base de données --")
        sale = Utils().retrieve_saler()
        Utils().print_queryset(sale)
        sale_contact_id = input("- ID du contact vendeur: ")
        
        amount = input("- Montant du contrat ")
        rest = amount
        status = "0"
        
        return {
            'customer_id': customer_id,
            'sale_contact_id': sale_contact_id,
            'amount': amount,
            'rest': rest,
            'status': status,
        }
        
    def contracts_view_update(self, contract):
        '''
        View contract update
        
        Args:
            contract (Contract): contract object
        '''

        Utils().clear_console()
        
        print("----------------------------------------------------------")
        print("----------------  Modifier le CONTRACT  -------------------") 
        print("----------------------------------------------------------")
        print("----------  Laissez le champ vide si inchangé  -----------")
        print("----------------------------------------------------------")
        
        print(f"ID du client: {contract.customer_id}")
        print("-- Clients présents dans la base de données --")
        Utils().retrieve_client()
        customer_id = input("- Modifier l'ID : ")
        print(f'ID contact vendeur : {contract.sale_contact_id}')
        print("-- Vendeurs présents dans la base de données --")
        sale = Utils().retrieve_saler()
        Utils().print_queryset(sale)
        sale_contact_id = input("- Modifier la Date de Début : ")
        print(f'Montant du contrat : {contract.amount}')
        amount = input("- Modifier le montant : ")
        print(f'Reste à régler : {contract.rest}')
        rest = input("- Modifier le reste : ")
        print(f'Status du contrat : ID: {contract.status}')
        status = input("- Modifier le status du contrat : ")
        
        return {
            'customer_id': customer_id,
            'sale_contact_id': sale_contact_id,
            'amount': amount,
            'rest': rest,
            'status': status,
        }
    