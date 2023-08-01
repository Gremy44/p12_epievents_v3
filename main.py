import sys

from controllers.start_cli import Start_Cli


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        cli = Start_Cli.start_cli_dev_mod()
    elif len(sys.argv) > 1 and sys.argv[1] == "soutenance":
        cli = Start_Cli.start_cli_soutenance_mod()
    else:
        cli = Start_Cli.start_cli_prod_mod()


if __name__ == "__main__":
    main()
