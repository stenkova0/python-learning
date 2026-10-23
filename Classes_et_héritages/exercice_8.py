import json

class Contact:
    def __init__(self, nom, numero):
        self.nom = nom
        self.numero = numero

    def __str__(self):
        return f"{self.nom} : {self.numero}"

    def appeler(self):
        print(f"Appel en cours vers {self.nom} au {self.numero}")

c = Contact("Alice", "0612345678")
print(c)
c.appeler()

with open("liste_de_contacts.json", "r") as liste:
    donnees = json.load(liste)
    listeContacts = []
    for chaque_contact in donnees:
        listeContacts.append(Contact(chaque_contact["nom"], chaque_contact["numero"]))

while True:
    print("Veuillez saisir votre option :\n 1 - Ajouter un contact\n 2 - Chercher un contact\n 3 - Appeler un contact\n 4 - Voir tous les contacts\n 5 - Sauvegarder et quitter")
    saisi_Menu = input()
    if saisi_Menu == "1":
        print("Veuillez saisir le nom du contact :")
        saisi_Nom = input()
        print("Veuillez saisir son numéro :")
        saisi_Numero = input()
        listeContacts.append(Contact(saisi_Nom, saisi_Numero))
        print("-----")
    if saisi_Menu == "2":
        print("Veuillez saisir le nom du contact que vous recherchez : ")
        saisi_Nom_Recherche = input()
        verification = ""
        for chaque_contact in listeContacts:
            if chaque_contact.nom == saisi_Nom_Recherche:
                print(chaque_contact)
                verification = "trouvé"

        if verification == "":
            print("Ce contact n'existe pas")
        print("-----")
    if saisi_Menu == "3":
        print("Veuillez saisir le nom du contact que vous voulez appeler : ")
        saisi_Nom_Appel = input()
        verification = ""
        for chaque_contact in listeContacts:
            if chaque_contact.nom == saisi_Nom_Appel:
                chaque_contact.appeler()
                verification = "trouvé"

        if verification == "":
            print("Ce contact n'existe pas")
        print("-----")
    if saisi_Menu == "4":
        for chaque_contact in listeContacts:
            print(chaque_contact)
    if saisi_Menu == "5":
        liste_en_dictionnaire = []
        for chaque_contact in listeContacts:
            liste_en_dictionnaire.append({"nom" : chaque_contact.nom, "numero" : chaque_contact.numero})
        
        with open("liste_de_contacts.json", "w") as fichier:
            json.dump(liste_en_dictionnaire, fichier)
        break