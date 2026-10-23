personnage = [
    {"nom": "Chen Qianyu", "type": "Physique"},
    {"nom": "Arcane", "type": "Nature"},
]

def affiche_operateur(personnage, saisi):
    affichage_message = ""
    for chaque_Operateur in personnage:
        if chaque_Operateur["nom"] == saisi:
            affichage_message = chaque_Operateur["type"]
    return affichage_message

print(affiche_operateur(personnage, "Chen Qianyu"))