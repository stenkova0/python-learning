import json

eleves = [
    {"nom": "Daniel", "note": 12},
    {"nom": "Samantha", "note": 18}
]

with open("donnees.json", "w") as fichier:
    json.dump(eleves, fichier)

print("Sauvegarde terminée")

with open("donnees.json", "r") as fichier:
    donnees = json.load(fichier)

print(donnees)