#Exercice 1
produits = [
    {"nom": "Pain", "prix": 1.20},
    {"nom": "Lait", "prix": 0.95},
    {"nom": "Fromage", "prix": 3.50},
    {"nom": "Beurre", "prix": 2.10},
    {"nom": "Eau", "prix": 0.50}
]

sommeProduit = float(0)
produit_Chère = float(0)
produit_Chère_N = ""

for produits_A in produits:
    sommeProduit = produits_A["prix"] + sommeProduit

    if produits_A["prix"] > produit_Chère:
        produit_Chère = produits_A["prix"]
        produit_Chère_N = produits_A["nom"]


print(sommeProduit)
print(produit_Chère)
print(produit_Chère_N)

print("--------")

#Exercice 2
prenoms = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

#for prenom in prenoms:
 #   prenomCaractere = len(prenom)
  #  print(f"{prenom} : {prenomCaractere}")

#Exercice 2-1 | Afficher les prénoms qui ont plus de 4 caractères
for prenom in prenoms:
    prenomCaractere = len(prenom)

    if prenomCaractere > 4:
        print(prenom)

print("--------")

#Exercice 3
temperatures = [15.5, 22.0, 18.3, 25.1, 19.8, 21.0, 16.7]
sommeTemperature = float(0)

for temperature in temperatures:
    sommeTemperature = temperature + sommeTemperature

temperatureTL = len(temperatures)
print(sommeTemperature/temperatureTL)

print("--------")

#Exercice 4
scores = [45, 78, 12, 93, 56, 88, 34]
scoresMax = int(0)

for score in scores:
    if score > scoresMax:
        scoresMax = score

print(scoresMax)

print("--------")

#Exercice 5
notes = [
    {"eleve": "Alice", "note": 14},
    {"eleve": "Bob", "note": 8},
    {"eleve": "Charlie", "note": 17},
    {"eleve": "Diana", "note": 11},
    {"eleve": "Eve", "note": 9}
]

tailleListe = len(notes)
moyenneNote = float(0)
meilleurEleve = ""
nombreEleve = int(0)
noteParEleve = int(0)

for noteE in notes :
    moyenneNote = noteE["note"] + moyenneNote
    if noteE["note"] > noteParEleve:
        noteParEleve = noteE["note"]
        meilleurEleve = noteE["eleve"]
    if noteE["note"] >= 10:
        nombreEleve = nombreEleve + 1

print (f"La moyenne de la classe est de : {moyenneNote/tailleListe}")
print (f"La meilleure note est de {noteParEleve}, détenu par : {meilleurEleve}")
print (f"{nombreEleve} élèves ont eu une note supérieure à 10.")

print("--------")

#Exercice 6
mots = ["python", "code", "apprentissage", "boucle", "variable", "fonction"]
longueurMot = int(0)
motLPL = ""

for motsL in mots:
    longueurListeMot = len(motsL)
    if longueurListeMot > longueurMot:
        longueurMot = longueurListeMot
        motLPL = motsL
print(motLPL)

print("--------")

#Exercice 7
ages = [25, 17, 34, 15, 42, 8, 19, 16, 30, 12]
nombre_Mineur = int(0)
nombre_Majeur = int(0)

for agesA in ages:
    if agesA >= 18:
        nombre_Majeur = nombre_Majeur + 1
    else:
        nombre_Mineur = nombre_Mineur + 1

print(f"Le nombre de mineur est de {nombre_Mineur}")
print(f"Le nombre de majeur est de {nombre_Majeur}")

print("--------")

#Exercice 8
ventes = [120, 85, 200, 150, 95, 310, 175]
totalVente = int(0)
meilleureVente = int(0)
nombre_Jour_Supp = int(0)

for ventesP in ventes:
    totalVente = ventesP + totalVente
    if ventesP > meilleureVente:
        meilleureVente = ventesP
    if ventesP > 150:
        nombre_Jour_Supp = nombre_Jour_Supp + 1

print(f"Le revenu total est de {totalVente}. La meilleure vente a été de {meilleureVente} et le nombre de jours où le bénéfice a été supérieur à 150 est de {nombre_Jour_Supp}.")