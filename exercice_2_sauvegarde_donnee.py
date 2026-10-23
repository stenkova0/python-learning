animaux = [
    {"nom": "Rex", "type": "chien"},
    {"nom": "Minou", "type": "chat"},
    {"nom": "Buddy", "type": "chien"},
    {"nom": "Felix", "type": "chat"},
    {"nom": "Max", "type": "chien"}
]

def compter_elements(liste, cle, valeur):
    compteur = int(0)
    for chaque_Animaux in liste:
        if chaque_Animaux[cle] == valeur:
            compteur = compteur + 1
    return compteur


print(compter_elements(animaux, "type", "chien"))  # 3
print(compter_elements(animaux, "type", "chat"))   # 2

animal = {"nom": "Rex", "type": "chien"}
cle = "type"
print(animal[cle])
print(animal["type"])