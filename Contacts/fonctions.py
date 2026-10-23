def affichage_liste_contacts(listeContacts):
    for chaque_Contacts in listeContacts:
        print(f"Nom : {chaque_Contacts["nom"]}, Numéro : {chaque_Contacts["numero"]}")

def recherche_contacts(listeContacts, saisi):
    stock_contacts = []
    for chaque_Contacts in listeContacts:
        if chaque_Contacts["nom"] == saisi:
            stock_contacts = chaque_Contacts
 
    if stock_contacts == []:
        print("Erreur de saisi")
    else:
        print(stock_contacts)

def suppression_contacts(listeContacts, saisi):
    stock_contacts = []
    for chaque_Contacts in listeContacts:
        if chaque_Contacts["nom"] == saisi:
            stock_contacts = chaque_Contacts
 
    if stock_contacts == []:
        print("Erreur de saisi")
    else:
        listeContacts.remove(stock_contacts)