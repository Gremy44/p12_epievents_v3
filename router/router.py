from controllers.login_controller import Login_Controller
# from controllers.users_controller import Users_Controller
# from controllers.contracts_controller import Contracts_Controller
# from controllers.events_controller import Events_Controller
from controllers.customers_controller import Customers_Controller

from views.generic_errors import Generic_Errors
from views.home import Home_view

from utils.utils import Utils

class Console:
    
    is_logged = False
    
    def __init__(self):
        pass
    
    def routing(self):
        '''
        function call in main.py to start the cli
        '''
        
        # loop until the user is logged
        while self.is_logged == False:
            
            login = Login_Controller()
            log = login.login()
            
            self.is_logged = log[0]
            user = log[1]
            
            if self.is_logged == False:
                Generic_Errors.login_error()
        
            
        
        while self.is_logged == True:
            
            self.user_choice = Home_view(user).home()
            
            if self.input_verification() == True:
                match self.user_choice[0]:
                    case '1':
                        Customers_Controller().customers_menu()
                    case '2':
                        print("C'est 2")
                        # Contracts_Controller().contracts()
                    case '3':
                        print("C'est 3")
                        # Events_Controller().events()
                    case '4':
                        print("C'est 4")
                        # Users_Controller().users()
            else:
                Generic_Errors().wrong_input()
                Utils().wait_user_input()
                Utils().clear_console()
        
    def input_verification(self):
        '''
        Check if the input is valid
        '''
        if self.user_choice[1][0] <= int(self.user_choice[0]) <= self.user_choice[1][1]:
            return True
        return False