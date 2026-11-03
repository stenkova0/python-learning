from bibliotheque import Bibliotheque
from gestionnaire import charger_liste_livre, ajouter_un_livre, afficher_recherche_livre, recherche_livre_return, sauvegarder_liste_livre

liste_livres = charger_liste_livre("bibliotheque.json")

while True:
    print("Veuillez saisir une option :\n 1 - Ajouter un livre\n 2 - Chercher un livre\n 3 - Voir tous les livres\n 4 - Passer un livre en lu et lui mettre une note\n 5 - Quitter et sauvegarder")
    saisi_Menu = input()
    if saisi_Menu == "1":
        print("Veuillez saisir le titre du livre :")
        saisi_Titre = input()
        print("Veuillez saisir son genre :")
        saisi_Genre = input()
        print("Veuillez saisir le nom de son auteur :")
        saisi_Auteur = input()
        ajouter_un_livre(liste_livres, saisi_Titre, saisi_Genre, saisi_Auteur)
        print("-----")
    if saisi_Menu == "2":
        print("Veuillez indiqué le titre du livre que vous recherchez :")
        saisi_Titre_Recherche = input()
        afficher_recherche_livre(liste_livres, saisi_Titre_Recherche)
        print("-----")
    if saisi_Menu == "3":
        for chaque_livre in liste_livres:
            print(chaque_livre)
        print("-----")
    if saisi_Menu == "4":
        print("Veuillez indiqué le titre du livre que vous recherchez : ")
        saisi_Titre_Recherche = input()
        recherche = recherche_livre_return(liste_livres, saisi_Titre_Recherche)
        recherche.est_lu()
        print("Veuillez saisir la note a attribué au livre :")
        saisi_Note_Livre = int(input())
        recherche.est_noter(saisi_Note_Livre)
        print("-----")
    if saisi_Menu == "5":
        sauvegarder_liste_livre("bibliotheque.json", liste_livres)
        print("-----")
        break