import subprocess

def check_pep8(folder_path, report_path):
    pycodestyle_cmd = ['pycodestyle', folder_path, '--exclude=env,pep8_report,migrations,database,.git,.vscode,.idea,__pycache__', '--max-line-length=109']
    report_file = open(report_path, 'w')

    try:
        subprocess.check_call(pycodestyle_cmd, stdout=report_file, stderr=subprocess.STDOUT)
        print("Vérification PEP 8 terminée. Aucune erreur trouvée.")
        report_file.write("Vérification PEP 8 terminée. Aucune erreur trouvée.")
    except subprocess.CalledProcessError as e:
        print("Vérification PEP 8 terminée. Erreurs trouvées.")
    finally:
        report_file.close()

if __name__ == "__main__":
    # Spécifiez le chemin du dossier contenant votre code
    code_folder_path = "./"

    # Spécifiez le chemin pour enregistrer le rapport PEP 8 au format .txt
    report_file_path = "./pep8_report/rapport_pep8.txt"

    check_pep8(code_folder_path, report_file_path)
