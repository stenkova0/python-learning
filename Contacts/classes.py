class Contact:
    def __init__(self, nom, numero):
        self.nom = nom
        self.numero = numero

    def afficher(self):
        print(f"Nom : {self.nom}, Numéro : {self.numero}")

#mon_contact = Contact("Alice", "0612345678")
#mon_contact.afficher()

liste = []
liste.append(Contact("Alice", "0612345678"))
liste.append(Contact("Bob", "0699887766"))

for chaque_Contacts in liste:
    chaque_Contacts.afficher()