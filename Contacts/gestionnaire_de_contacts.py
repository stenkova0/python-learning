import json
from fonctions import affichage_liste_contacts, recherche_contacts, suppression_contacts

with open("liste_de_contacts.json", "r") as liste:
    listeContacts = json.load(liste)

while True:
    print("Bonjour veuillez choisir votre option :\n 1 - Ajouter un contact\n 2 - Recherchez un contact\n 3 - Afficher les contacts\n 4 - Supprimer un contact\n 5 - Quitter")
    saisi_Menu = input()
    if saisi_Menu == "1":
        print("Veuillez saisir le nom de votre contact :")
        saisi_Nom = input()
        print("Veuillez saisir le numéro de téléphone de ce contact :")
        saisi_Numero = input()
        listeContacts.append({"nom": saisi_Nom, "numero": saisi_Numero})
        print("------")
    if saisi_Menu == "2":
        print("Veuillez saisir le nom de la personne que vous recherchez :")
        saisi_Nom_Recherche = input()
        recherche_contacts(listeContacts, saisi_Nom_Recherche)
        print("------")
    if saisi_Menu == "3":
        affichage_liste_contacts(listeContacts)
        print("------")
    if saisi_Menu == "4":
        print("Veuillez saisir le nom de la personne que vous souhaitez supprimer :")
        saisi_Nom_Recherche_Suppr = input()
        suppression_contacts(listeContacts, saisi_Nom_Recherche_Suppr)
    if saisi_Menu == "5":
        with open("liste_de_contacts.json", "w") as fichier:
            json.dump(listeContacts, fichier)
        break