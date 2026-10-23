inventaire = [
    {"produit": "Clavier", "stock": 15, "prix": 45.00},
    {"produit": "Souris", "stock": 0, "prix": 25.00},
    {"produit": "Écran", "stock": 3, "prix": 250.00},
    {"produit": "Casque", "stock": 8, "prix": 75.00},
    {"produit": "Webcam", "stock": 0, "prix": 60.00}
]

# Le programme demande un nom de produit à l'utilisateur. S'il existe et est en stock (stock supérieur à 0), il affiche le prix et réduit le stock de 1. 
# S'il existe mais le stock est à 0, il dit que le produit est en rupture. 
# S'il n'existe pas, il le dit.

print("Bonjour, veuillez indiquer un nom de produit : ")
saisi_Produit = input()

def analyse_inventaire(inventaire, saisi):

    affichage_Message = ""

    for chaque_Inventaire in inventaire:
        if chaque_Inventaire["produit"] == saisi:
            if chaque_Inventaire["stock"] > 0 :
                affichage_Message = f"Le prix pour {chaque_Inventaire["produit"]} est de {chaque_Inventaire["prix"]}, le stock est de {chaque_Inventaire["stock"]} et va être réduit de 1"
                chaque_Inventaire["stock"] = chaque_Inventaire["stock"] - 1
            else:
                affichage_Message = "Ce produit existe, mais il est en rupture !"
            
    if affichage_Message == "":
        affichage_Message = "Ce produit n'existe pas"
        
    return affichage_Message

print(analyse_inventaire(inventaire, saisi_Produit))