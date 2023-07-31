from utils.utils import Utils
from views.generic_errors import Generic_Errors

class Events_View:
    def __init__(self):
        pass
    
    def events_id_input(self):
        return input("Entrer l'id de l'Evènement : ")
    
    def events_add_validate(self):
        print("L'Evènement' a bien été ajouté !")
        Utils().wait_user_input()
        
    def events_update_validate(self):
        print("L'Evènement' a bien été modifié !")
        Utils().wait_user_input()
        
    def events_delete_validate(self):
        print("L'Evènement' a bien été supprimé !")
        Utils().wait_user_input()
        
    def events_crud_action(self):
        print('----------------------------')
        print("1 - Détail d'un Evènement")
        print('2 - Ajouter un Evènement')
        print('3 - Modifier un Evènement')
        print('4 - Supprimer un Evènement')
        print('5 - Retour')
        print('----------------------------')
    
    def events_view_list(self, table_name, events, user):
        '''
        View events
        
        Returns:
            tuple: choix:str, id_customer:int
        '''
        Utils().clear_console()
        
        print("----------------------------------------------------------") # 58
        print(f"----------------------{table_name}-------------------------") # 
        print("----------------------------------------------------------") # 58
        print(user.role_id)
        
        for event in events:
            try:
                print(f"ID : {event.id}|Nom de l'évènement: {event.name}|Lieu: {event.location}|Client: {event.client.complet_name}|Contrat: {event.contract.id}|Contacte support: {event.support_contact.first_name} {event.support_contact.last_name}")
            except AttributeError:
                print(f"ID : {event.id}|Nom de l'évènement: {event.name}|Lieu: {event.location}|Client: {event.client.complet_name}|Contrat: {event.contract.id}|Contacte support: Aucun")

        if user.role_id == 3 :
            print("- Event sans contact support :")
            for ns in events:
                if ns.support_contact_id == "":
                    print(f"ID : {ns.id}|Nom de l'évènement: {ns.name}|Lieu: {ns.location}|Client: {ns.client.complet_name}|Contrat: {ns.contract.id}")
        
        if user.role_id == 2 :
            print("Vos Evènements :")
            for me in events:
                if me.support_contact_id == user.id:
                    print(f"ID : {me.id}|Nom de l'évènement: {me.name}|Lieu: {me.location}|Client: {me.client.complet_name}|Contrat: {me.contract.id}")
                
        self.events_crud_action()
                
        return input("Votre choix : ")
    
    def events_view_detail(self, event):
        '''
        View event details
        
        Args:
            event (Event): event object
        '''
        Utils().clear_console()
        
        print(f'ID : {event.id}')
        print(f"Nom de l'évènement : {event.name}")
        print(f'Date de commencement : {event.date_start}')
        print(f'Date de fin : {event.date_end}')
        print(f'Lieu : {event.location}')
        print(f'Nombre de personnes attendues : {event.attendees}')
        print(f'Notes : {event.notes}')
        print(f'Client : {event.client.complet_name}')
        print(f'Contrat associé : {event.contract.id}')
        print(f'Contacte support :')
        print(f' - ID:{event.support_contact.id}')
        print(f' - Nom:{event.support_contact.last_name} Prénom :{event.support_contact.first_name}')
        print("----------------------------------------------------------")
        Utils().wait_user_input()
        
    def events_view_add(self):
        '''
        View event add
        
        Args:
            table_name (str): table name
        '''
        Utils().clear_console()
        
        print("----------------------------------------------------------") # 58
        print("------------------  Nouvel Evènement  --------------------") # 
        print("----------------------------------------------------------") # 58
        
        name = input("- Nom de l'Evènement: ")
        date_start = input("- Date de début (JJ/MM/AAAA): ")
        date_end = input("- Date de fin (JJ/MM/AAAA): ")
        location = input("- Lieu : ")
        attendees = input("- Nombre de personnes attendues : ")
        notes = input("- Note : ")
        print("ID Client associé :")
        print("Clients présents dans la base de données :")
        Utils().retrieve_client()
        client_id = input("- ID client : ")
        print("ID Contrat associé :")
        print("Contrats présents et valide dans la base de données pour ce client:")
        Utils().retrieve_contract(client_id)
        contract_id = input("- ID contrat : ")
        print("ID Contacte support :")
        support = Utils().retrieve_support()
        Utils().print_queryset(support)
        support_contract_id = input("- ID Contact support : ")
        
        
        return {
            'name': name,
            'date_start': date_start,
            'date_end': date_end,
            'location': location,
            'attendees': attendees,
            'notes': notes,
            'client_id': client_id,
            'contract_id': contract_id,
            'support_contact_id': support_contract_id,
        }

    
    def events_view_update(self, event):
        '''
        View event update
        
        Args:
            event (Event): event object
        '''

        Utils().clear_console()
        
        print("----------------------------------------------------------")
        print("----------------  Modifier Evènement  --------------------") 
        print("----------------------------------------------------------")
        print("----------  Laissez le champ vide si inchangé  -----------")
        print("----------------------------------------------------------")
        
        print(f"Nom de l'Evènement: {event.name}")
        name = input("- Modifier le Nom : ")
        print(f'Date de début : {event.date_start}')
        date_start = input("- Modifier la Date de Début : ")
        print(f'Date de fin : {event.date_end}')
        date_end = input("- Modifier la Date de Fin : ")
        print(f'Lieu : {event.location}')
        location = input("- Modifier le Lieu : ")
        print(f'Personnes attendus : ID: {event.attendees}')
        attendees = input("- Modifier le Nombre de Personnes Attendus : ")
        print(f'Notes : ID: {event.notes}')
        notes = input("- Modifier les Notes : ")
        print(f'Client associé : ID: {event.client_id}')
        client_id = input("- Modifier le Client Associé : ")
        print(f'Contrat associé : ID: {event.contract_id}')
        contract_id = input("- Modifier le Contrat Associé : ")
        print(f'Contacte support : ID: {event.support_contact_id}')
        support_contact_id = input("- Modifier Contact Support : ")
        
        return {
            'name': name,
            'date_start': date_start,
            'date_end': date_end,
            'location': location,
            'attendees': attendees,
            'notes': notes,
            'client_id': client_id,
            'contract_id': contract_id,
            'support_contact_id': support_contact_id,
        }
