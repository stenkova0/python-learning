from compte import Compte
import json

def charger_compte(fichier):
    with open(fichier, "r", encoding="utf-8") as liste_compte:
        comptes = json.load(liste_compte)

    liste_compte_objet = []
    for chaque_compte in comptes:
        liste_compte_objet.append(Compte(chaque_compte["titulaire"], chaque_compte["solde"]))

    return liste_compte_objet

def ajouter_compte(liste_compte, titulaire, solde):
    liste_compte.append(Compte(titulaire, solde))

def chercher_compte(liste_compte, titulaire):
    for chaque_compte in liste_compte:
        if chaque_compte.titulaire.lower() == titulaire.lower():
            return chaque_compte

def demander_nombre(message):
    while True:
        try:
            print(message)
            resultat_demande = int(input())
            return resultat_demande
        except ValueError:
            print("Veuillez saisir un chiffre")

def sauvegarde_comptes(fichier, liste_compte):
    liste_compte_dict = []
    for chaque_compte in liste_compte:
        liste_compte_dict.append({"titulaire": chaque_compte.titulaire, "solde": chaque_compte.solde})

    with open(fichier, "w") as fichier_json:
        json.dump(liste_compte_dict, fichier_json)