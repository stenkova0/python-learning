contacts = [
    {"nom": "Alice", "tel": "0612345678", "ville": "Paris"},
    {"nom": "Bob", "tel": "0698765432", "ville": "Lyon"},
    {"nom": "Charlie", "tel": "0655443322", "ville": "Paris"},
    {"nom": "Diana", "tel": "0611223344", "ville": "Marseille"}
]

# Le programme demande un nom de ville à l'utilisateur et affiche tous les contacts qui habitent dans cette ville. S'il n'y a aucun contact dans cette ville, il le dit.

print("Bonjour. Veuillez saisir un nom de ville : ")
saisi_Contact = input()

def analyse_contacts(contacts, saisi):

    affichage_information = ""
    liste_Contacts = []

    for chaque_Contacts in contacts:
        if chaque_Contacts["ville"] == saisi:
            liste_Contacts.append(chaque_Contacts)

    taille_liste = len(liste_Contacts)

    if taille_liste > 0:
        affichage_information = liste_Contacts
    else:
        affichage_information = "Il n'y a personne dans cette ville"
    return affichage_information

print(analyse_contacts(contacts, saisi_Contact))
