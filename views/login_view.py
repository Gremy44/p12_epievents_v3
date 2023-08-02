from utils.utils import Utils
import getpass
from utils.validators import Validators
import sys


class Login_view:
    def __init__(self):
        self.validator = Validators()

    def login(self):
        while True:
            Utils().clear_console()

            print("----------------------------------------------------------")  # 58
            print("----------------------   WELCOM  -------------------------")  #
            print("----------------------------------------------------------")
            print("--------------------- LOGIN OR QUIT-----------------------")  # 58
            print("----------------------------------------------------------")
            print("1 - Login")
            print("2 - Quit")

            choice = self.validator.validator_menu_choice(1, 2)

            if choice == "1":
                email = input("- Enter your email : ")
                password = getpass.getpass("- Enter your password : ")
                return (email, password)
            else:
                input("Bye bye !")
                Utils().clear_console()
                # sys.exit()
                break
