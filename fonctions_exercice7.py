commandes = [
    {"client": "Alice", "montant": 45.00, "livre": True},
    {"client": "Bob", "montant": 120.00, "livre": False},
    {"client": "Charlie", "montant": 15.00, "livre": True},
    {"client": "Diana", "montant": 85.00, "livre": False},
    {"client": "Eve", "montant": 200.00, "livre": True}
]

def analyse_commandes (commandes):
    total_montant = int(0)
    nb_commandes_en_attente = int(0)
    comparateur_montant = int(0)

    nom_client_eleve = ""

    for chaque_Commande in commandes:
        if chaque_Commande["livre"] == False:
            nb_commandes_en_attente = nb_commandes_en_attente + 1
            if chaque_Commande["montant"] > comparateur_montant:
                comparateur_montant = chaque_Commande["montant"]
                nom_client_eleve = chaque_Commande["client"]
        else:
            total_montant = total_montant + chaque_Commande["montant"]

    return total_montant, nb_commandes_en_attente, nom_client_eleve

print(analyse_commandes(commandes))