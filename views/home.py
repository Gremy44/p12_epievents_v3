from views.generic_errors import Generic_Errors
from utils.utils import Utils
import sys

class Home_view:
    def __init__(self, user):
        self.user = user
        self.quit_message = "CIAO !! Press any key to exit"
    
    def home(self):
        '''
        Display the home view
        '''
        Utils().clear_console()
        
        print("----------------------------------------------------------") # 58
        print("----------------------    HOME   -------------------------") # 
        print("----------------------------------------------------------") # 58
        
        if self.user.is_superuser == True:
            return self.menu_admin()
            
        elif self.user.is_superuser == False and self.user.role_id == 1:
            return self.menu_sale()
            
        elif self.user.is_superuser == False and self.user.role_id == 2:
            return self.menu_support()
            
        elif self.user.is_superuser == False and self.user.role_id == 3:
            return self.menu_gestion()
            
        else:
            Generic_Errors().unknown_role()
            
    def menu_admin(self):
        '''
        Display the admin menu
        '''
        print(f"ADMIN-{self.user.first_name}----------------------------------------------------")
        print("1 - Gestion des Clients")
        print("2 - Gestion des Contrats")
        print("3 - Gestion des Evènements")
        print("4 - Gestion des Utilisateurs")
        print("5 - Quitter")
        
        rep = input("Votre choix : ")
        
        if rep == '5':
            Utils().clear_console()
            input(self.quit_message)
            sys.exit()
            
        return (rep, (1,4))
            
    def menu_sale(self):
        '''
        Display the sale menu
        '''
        print(f"SALE-{self.user.first_name}------------------------------------------------------")
        print("1 - Gestion des Clients")
        print("2 - Gestion des Contrats")
        print("3 - Gestion des Evènements")
        print("4 - Quitter")
        
        rep = input("Votre choix : ")
        
        if rep == '4':
            Utils().clear_console()
            input(self.quit_message)
            sys.exit()
            
        return (rep, (1,3))
        
    def menu_support(self):
        '''
        Display the support menu
        '''
        print(f"SUPPORT-{self.user.first_name}--------------------------------------------------")
        print("1 - Gestion des Clients")
        print("2 - Gestion des Contrats")
        print("3 - Gestion des Evènements")
        print("4 - Quitter")
        
        rep = input("Votre choix : ")
        
        if rep == '4':
            Utils().clear_console()
            input(self.quit_message)
            sys.exit()
            
        return (rep, (1,3))
        
    def menu_gestion(self):
        '''
        Display the gestion menu
        '''
        print(f"GESTION-{self.user.first_name}--------------------------------------------------")
        print("1 - Gestion des Clients")
        print("2 - Gestion des Contrats")
        print("3 - Gestion des Evènements")
        print("4 - Gestion des Utilisateurs")
        print("5 - Quitter")
        
        rep = input("Votre choix : ")
        
        if rep == '5':
            Utils().clear_console()
            input(self.quit_message)
            sys.exit()
            
        return (rep, (1,4))
