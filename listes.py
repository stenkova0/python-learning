#Les listes
listePrenom = ["Pascale", "Jean", "Amélie", "Thibault"]
print(listePrenom) #Affiche la liste des prénoms
print(listePrenom[0]) #Affiche ce que contient la cellule 0 (si on connaît la taille de la liste)
print(listePrenom[3])
print("---------")

print(listePrenom[-1]) #Affiche ce que contient la dernière cellule, même si on ne connaît pas la taille de la liste
print(listePrenom[-2]) #Affiche ce que contient l'avant-dernière cellule, et ainsi de suite
print("---------")

print(len(listePrenom)) #Affiche le nombre d'éléments dans la liste
listePrenom.append("Sergeï") #Ajouter un prénom à la liste
print(listePrenom) #Affiche la liste avec le prénom en plus
print(len(listePrenom)) #Affiche la nouvelle taille de la liste
listePrenom.remove("Sergeï") #Supprime le prénom à la liste
print(listePrenom) #Affiche la liste sans le prénom
print(len(listePrenom)) #Affiche la nouvelle taille de la liste
print("---------")

#listePrenom.pop(1) #Supprime l'élément de la cellule 1
#print(listePrenom)
#print("---------")

print(listePrenom[0:2])
print(listePrenom[1:3])
print(listePrenom[:2])
print(listePrenom[2:])

print("---------")

for prenom in listePrenom:
    print(prenom)

print("---------")

listeChiffre = [1,2,3,4,5,6,7,8,9,10]
for chiffre in listeChiffre:
    if chiffre%2 == 0:
        print(chiffre)

print("---------")

#Les dictionnaires
personne = {"prenom": "Jean", "age": 31, "ville": "Paris"} #Création d'un dictionnaire
print(personne["prenom"]) #Affichage du prénom contenu dans le dictionnaire
# personne_Prenom = personne.get("prenom") #Même méthode que la précédente, mais plus complexe
# print(personne_Prenom)

#Modifier et/ou ajouter des valeurs au dictionnaire
personne["ville"] = "Lyon"
personne["métier"] = "Agent de sécurité"

# personne.update({"ville": "Lyon"}) #update est utile, mais est plus utilisé pour modifier plusieurs valeurs
# personne.update({"metier": "Agent de sécurité"})
print(personne)

for cle in personne:
    print(f"{cle} : {personne[cle]}")

print("---------")

#Les Tuples
coordonnees = (48.8, 2.3)
print(coordonnees[0])
#coordonnees[0] = 50.0 - Les données d'un Tuple ne peuvent être changé, donc cette ligne ne fonctionne pas
print("---------")

#Les Sets
nombres = [1, 2, 3, 2, 4, 3, 5, 1]
nombres_uniques = set(nombres)
print(nombres)
print(nombres_uniques)

fruits_alice = {"pomme", "banane", "orange"}
fruits_bob = {"banane", "kiwi", "pomme"}
print(fruits_alice & fruits_bob)
print(fruits_alice | fruits_bob)

#Compréhension de listes
#On veut avoir le résultat au carré pour chacun des nombres de la listes_Nombres. Dans un premier temps on le fait de manière conventionnelle
listes_Nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listes_Nombres_AC = []
print(listes_Nombres_AC)

#for chiffre_AC in listes_Nombres:
 #   chiffre_Calcul = chiffre_AC*chiffre_AC 
  #  listes_Nombres_AC.append(chiffre_Calcul)
   # print(listes_Nombres_AC)

#Maintenant voici une version plus rapide propre à Python
listes_Nombres_AC = [chiffre_AC * chiffre_AC for chiffre_AC in listes_Nombres]
#Un autre exemple si on veut garder que les pairs dans une variable
pairs = [x for x in listes_Nombres if x%2 == 0]
print(pairs)
print("---------")

#Exercice
eleves = [
    {"nom": "Alice", "note": 15},
    {"nom": "Bob", "note": 8},
    {"nom": "Charlie", "note": 12},
    {"nom": "Diana", "note": 6},
    {"nom": "Eve", "note": 17}
]

note_Sup = [note_Sup_10["nom"] for note_Sup_10 in eleves if note_Sup_10["note"] >= 10]
print(note_Sup)

#for note_Sup_10 in eleves:
 #   print(note_Sup_10)