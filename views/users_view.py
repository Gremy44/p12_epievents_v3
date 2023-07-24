from utils.utils import Utils

class User_View:
    def __init__(self):
        pass
    
    def users_id_input(self):
        return input("Entrer l'id de l'utilisateur : ")
    
    def users_add_validate(self):
        print("L'utilisateur a bien été ajouté !")
        Utils().wait_user_input()
        
    def users_update_validate(self):
        print("L'utilisateur' a bien été modifié !")
        Utils().wait_user_input()
        
    def users_delete_validate(self):
        print("L'utilisateur' a bien été supprimé !")
        Utils().wait_user_input()
        
    def users_crud_action(self):
        print('----------------------------')
        print("1 - Détail d'un utilisateur")
        print('2 - Ajouter un utilisateur')
        print('3 - Modifier un utilisateur')
        print('4 - Supprimer un utilisateur')
        print('5 - Retour')
        print('----------------------------')
        
    def users_view_list(self, table_name, users):
        '''
        View users
        
        Returns:
            tuple: choix:str, id_users:int
        '''
        Utils().clear_console()
        
        print("----------------------------------------------------------") # 58
        print(f"----------------------{table_name}-------------------------") # 
        print("----------------------------------------------------------") # 58
        
        for user in users:
            print(f"N°: {user.id}|Nom: {user.last_name}|Prenom: {user.first_name}|Role: {user.role.role}")
    
        self.users_crud_action()
                
        return input("Votre choix : ")
    
    def users_view_detail(self, user):
        '''
        View user details
        
        Args:
            user(user): user query
        '''
        Utils().clear_console()
        print(f'ID : {user.id}')
        print(f'Nom : {user.last_name}')
        print(f'Prénom : {user.first_name}')
        print(f'Email : {user.email}')
        print(f'Actif : {user.is_active}')
        print(f'Date création : {user.date_created}')
        print(f'Dernière connexion : {user.last_login}')
        print(f'Role : {user.role.role}')
        print("----------------------------------------------------------")
        Utils().wait_user_input()
        
    def users_view_add(self):
        '''
        View user add
        
        Args:
            table_name (str): table name
        '''
        Utils().clear_console()
        
        print("----------------------------------------------------------") # 58
        print("----------------  Nouvel utilisateur  --------------------") # 
        print("----------------------------------------------------------") # 58
        
        return {
            'last_name': input("- Nom : "),
            'first_name': input("- Prénom : "),
            'email': input("- Email : "),
            'password': input("- Mot de passe : "),
            'role': input("- Role (1-Vendeur|2-Support|3-Gestion): "),
        }
        
    def users_view_update(self, user):
        '''
        View user update
        
        Args:
            user(User): user object
        '''

        Utils().clear_console()
        
        print("----------------------------------------------------------")
        print("---------------  Modifier l'utilisateur  -----------------")
        print("----------------------------------------------------------")
        print("----------  Laissez le champ vide si inchangé  -----------")
        print("----------------------------------------------------------")
    
        print(f'Nom : {user.last_name}')
        last_name = input("- Modifier le nom : ")
        print(f'Prénom : {user.first_name}')
        first_name = input("- Modifier le prénom : ")
        print(f'Email : {user.email}')
        email = input("- Modifier le mail : ")
        print(f'Mot de passe :')
        password = input("- Modifier le mot de passe : ")
        print(f'Role : {user.role.role}')
        role_id = input("- Modifier le role (1-Vendeur|2-Support|3-Gestion): ")
        
        return {
            'last_name': last_name,
            'first_name': first_name,
            'email': email,
            'password': password,
            'role_id': role_id,
        }