commandes = [
    {"client": "Alice", "montant": 45.00, "livre": True},
    {"client": "Bob", "montant": 120.00, "livre": False},
    {"client": "Charlie", "montant": 15.00, "livre": True},
    {"client": "Diana", "montant": 85.00, "livre": False},
    {"client": "Eve", "montant": 200.00, "livre": True}
]

print("Veuillez saisir le nom du client : ")
nom_Saisi = input()

def trouver_client (commandes, nom):
    for chaque_Commandes in commandes:
        if chaque_Commandes["client"] == nom:
            return chaque_Commandes


resultat = trouver_client(commandes, nom_Saisi)

if resultat != None:
    print(trouver_client(commandes, nom_Saisi))
else:
    print("Erreur de saisi")
