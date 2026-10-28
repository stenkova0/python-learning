from compte import Compte
from gestionnaire import charger_compte, ajouter_compte, chercher_compte, sauvegarde_comptes

liste_comptes = charger_compte("comptes.json")

while True:
    print("Veuillez saisir une option :\n 1 - Ajouter un compte\n 2 - Déposer un montant\n 3 - Retirer un montant\n 4 - Voir le solde d'un compte\n 5 - Sauvegarder et quitter")
    saisi_Menu = input()

    #Ajouter un compte
    if saisi_Menu == "1":
        print("Veuillez indiquer le nom du titulaire :")
        saisi_Nom_Titulaire = input()
        print("Veuillez saisir son solde :")
        saisi_Solde_Titulaire = int(input())
        ajouter_compte(liste_comptes, saisi_Nom_Titulaire, saisi_Solde_Titulaire)
        print("-----")

    #Déposer un montant
    if saisi_Menu == "2":
        print("Veuillez saisir le nom du titulaire dont vous voulez déposer un montant :")
        saisi_Nom_Titulaire_Deposer_Montant = input()

        compte_trouver = chercher_compte(liste_comptes, saisi_Nom_Titulaire_Deposer_Montant)
        if compte_trouver != None:
            print("Veuillez saisir le montant à déposer :")
            saisi_Solde_Deposer_Montant = int(input())
            compte_trouver.deposer(saisi_Solde_Deposer_Montant)
        else:
            print("Ce titulaire n'existe pas")

        print("-----")

    #Retirer un montant
    if saisi_Menu == "3":
        print("Veuillez saisir le nom du titulaire dont vous voulez retirer un montant :")
        saisi_Nom_Titulaire_Retirer_Montant = input()

        compte_trouver = chercher_compte(liste_comptes, saisi_Nom_Titulaire_Retirer_Montant)
        if compte_trouver != None:
            print("Veuillez saisir le montant à retirer :")
            saisi_Solde_Retirer_Montant = int(input())
            compte_trouver.retirer(saisi_Solde_Retirer_Montant)
        else:
            print("Ce titulaire n'existe pas")

        print("-----")

    #Voir le solde d'un compte
    if saisi_Menu == "4":
        print("Veuillez saisir le nom du titulaire dont vous voulez voir le solde :")
        saisi_Nom_Titulaire_Recherche = input()

        compte_trouver = chercher_compte(liste_comptes, saisi_Nom_Titulaire_Recherche)
        if compte_trouver != None:
            print(compte_trouver)
        else:
            print("Ce titulaire n'existe pas")

        print("-----")

    #Sauvegarder et quitter
    if saisi_Menu == "5":
        sauvegarde_comptes("comptes.json", liste_comptes)
        print("-----")
        break