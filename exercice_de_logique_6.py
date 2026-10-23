def calculer_surface(longueur, largeur):
    surface = longueur * largeur
    return surface

def calculer_peinture(longueur, largeur, couches):
    quantite = calculer_surface(longueur, largeur) * couches
    return quantite

print(calculer_peinture(5, 3, 2))   # 30 (surface 15 × 2 couches)