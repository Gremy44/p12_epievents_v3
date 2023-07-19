from controllers.start_cli import Start_Cli
from config import Session

database_path = 'database\database.db'

if __name__ == "__main__":

    cli = Start_Cli.start_cli_dev_mod()
