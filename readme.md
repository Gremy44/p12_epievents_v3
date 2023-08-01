# Projet 12 - Epic Events
## Sommaire :
- Introduction
- Mise en place
- Fonctionnement
- Utilisation
- Journalisation

#### 1 - Introduction
Projet réaslisé dans le cadre de la formation développeur d'applications Python de Open Classrooms. Il met en situation la création d'une application CMS pour la gestion d'évènements. Celle-ci doit permettre de gérer les clients, les contrats, les évènements ainsi que les utilisateurs de la plateforme. L'application utilise la stack suivante : 
- Base de données : Sqlite
- ORM : SqlAlchemy
- Interface : invite de commande
- Journalisation : Sentry

#### 2 - Mise en place 
Après avoir **cloné** le repository Github, créez votre environnement vituel et installez les librairie présentent dans le fichier `requirements.txt`.
Pour activer la journalisation avec Sentry, créez un compte sur le site si vous n'en avez pas et ajouter le projet à votre dashboard.
Dans la racine du projet, créez un fichier `.env` avec le nom de votre DSN comme suit : `SENTRY_DSN="votre dsn"`.
Pour démarrer le projet, dans me répertoire du projet, exectuez la commande `python main.py`

#### 3 - Fonctionnement
L'application a 3 'profils' différents que vous pouvez utiliser:
- *'dev'* accessible en executant `python main.py dev`
- *'soutenance'* accessible en executant `python main.py soutenance`
- *'production'* accessible en executant `python main.py`

> **/!\ ATTENTION /!\\** Les 3 profils écrivent leur base de données à la même adresse. Les profils *'dev'* et *'soutenance'* n'ont pas de base données persistante, si vous commencez à créer une base de donné en mode 'production', et que vous utilisez un de ces deux profil ensuite, vous **perdrez** vos données de production.

les trois profils sont livrés avec un profil Admin à l'execution, accessible avec les id suivants : 
> ID : admin@email.com
> MDP : admin

**Le profil 'dev'**
J'utilise ce profile pour tester mon interface, mes manipulation CRUD, etc... à l'execution, la base de données précédente est automatiquement écrasée et pré-rempli avec des **seeders** pour toutes les tables. 

**Le profil 'soutenance'**
Je l'utilise pour le UserCase de ma soutenance de projet. Il crée une nouvelle base de données à chaque execution en supprimant la précédente et ses tables sont pré-rempli pour m'aider dans ma démonstration de soutenance. A part pour ma soutenance, il n'aura pas d'utilité en développement ou en production. 

**Le profil 'production'**
C'est le profil principal, avec une base donnée persistente. Il reflête le fonctionnement normal de l'application. Ses tables sont vides à l'exception du profil Admin.

>**SECURITE**
>Comme demandé dans l'exercice, les mot de passe sont écris en crypté dans la base de donnée, 'salé' et 'hashé' avec argon2

## 4 - Utilisation

**Au démarrage de l'application**
Une fois le profile choisi vous arriverez dans un premier menu qui vous propose soit de vous logger soit de quitter l'application. 

**Loggin**
Saisissez vos identifiant pour vous logger. Pour la première connexion, utilisez le profil admin pour acceder à l'application et créer d'autres Utilisateurs. 

**Menu pricipale**
Une fois loggé vous arrivez dans le menu principal, duquel vous pourrez effectuer les opérations qui seront disponibles selon votre rôle ('Sale', 'Support' ou 'Gestion').

### 5 - Journalisation
La journalisation avec Sentry se fait automatiquement, comme demandé dans l'exercice et vous enverra des alertes si une erreur fait planter l'application, si un utilisateur est ajouté ou modifié et si un contrat est signé.

