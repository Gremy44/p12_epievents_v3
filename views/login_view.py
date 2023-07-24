from utils.utils import Utils
import getpass

class Login_view:
    
    def __init__(self):
        pass
    
    def login(self):
        Utils().clear_console()
        
        print("----------------------------------------------------------") # 58
        print("----------------------   WELCOM  -------------------------") # 
        print("----------------------------------------------------------") # 58
        
        email = input("- Enter your email : ")
        password = getpass.getpass("- Enter your password : ")
        return (email, password)