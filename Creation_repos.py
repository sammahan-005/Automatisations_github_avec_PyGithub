import os
from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("your secret token")  # Remplacez par votre token d'accès personnel GitHub

# Public Web Github
g = Github(auth=auth)

try:
    user = g.get_user() # Récupère l'utilisateur authentifié
    print(f"Connexion réussie ! Nom d'utilisateur: {user.login}")
except Exception as e:
    print(f"Échec de l'authentification : {e}")
    exit()

def Creer_repos(name,description,priv):
    
#Creation d'un repository

# name = input("Entrez le nom du repository à créer: ")
# description = input("Entrez la description du repository: ")
# priv = input("Le repository doit-il être privé ? (oui/non): ").lower()

    priv = priv.lower()

    if priv == 'oui':
        priv = True
        try:
            repo = user.create_repo(
                name=name,
                description=description,
                private=priv
            )
            print(f"Repository privé '{name}' créé avec succès.")
            return True
            
        except Exception as e:
            print(f"Échec de la création du repository privé : {e}")
            return e
               
    elif priv == 'non':
        priv = False
        try:
            repo = user.create_repo(
                name=name,
                description=description,
                private=priv
            )
            print(f"Repository public '{name}' créé avec succès.")
            return True
        except Exception as e:
            print(f"Échec de la création du repository public : {e}")
            return e    
    else:
        print("Entrée invalide pour la confidentialité du repository. Veuillez entrer 'oui' ou 'non'.")
        return "Entrée invalide pour la confidentialité du repository. Veuillez entrer 'oui' ou 'non'."
    
         