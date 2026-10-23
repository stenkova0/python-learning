def dire_bonjour(prenom):
    print(f"Bonjour {prenom} !")

dire_bonjour("Alice")
dire_bonjour("Bob")

print("--------")

def calculer_carre(nombre):
    return nombre * nombre
print(calculer_carre(5))

print("--------")

def calculer_moyenne(nombreA):
    nombre_Addition = int(0)
    liste_Nombre = len(nombreA)
    for unNombre in nombreA:
        nombre_Addition = unNombre + nombre_Addition
    return nombre_Addition/liste_Nombre

print(calculer_moyenne([15, 20, 8, 12, 18]))

print("--------")

def trouver_max(liste_Nombre):
    nombre_Max = int(0)
    for chaque_Nombre in liste_Nombre:
        if chaque_Nombre > nombre_Max:
            nombre_Max = chaque_Nombre
    return nombre_Max

print(trouver_max([45, 78, 12, 93, 56]))

print("--------")

def analyser_notes(liste_nombre_A):
    moyenne_Final = int(0)
    taille_Liste = len(liste_nombre_A)
    meilleure_Note = int(0)
    note_Superieur_10 = int(0)

    for chaque_nombre_A in liste_nombre_A:
        moyenne_Final = chaque_nombre_A + moyenne_Final
        if chaque_nombre_A > 10:
            note_Superieur_10 = note_Superieur_10 + 1
        if chaque_nombre_A > meilleure_Note:
            meilleure_Note = chaque_nombre_A
    return moyenne_Final/taille_Liste, meilleure_Note, note_Superieur_10

moyenne, meilleure, nb_sup = analyser_notes([14, 8, 17, 11, 9])
print(f"Moyenne : {moyenne}, Meilleure : {meilleure}, Au-dessus de 10 : {nb_sup}")

print("--------")

def compter_voyelles(liste_Mot_A):
    nombre_Voyelle = int(0)

    for un_Mot in liste_Mot_A:
        if un_Mot in "aeiouy":
            nombre_Voyelle = nombre_Voyelle + 1
    return nombre_Voyelle

print(compter_voyelles("bonjour"))
print(compter_voyelles("python"))

print("--------")

def repeter_mot(mot_a_afficher, nb_Rep = 2):
    for repetition in range(nb_Rep):
        print(mot_a_afficher)

repeter_mot("salut", 5)   # affiche 5 fois
repeter_mot("bonjour")    # affiche 2 fois (valeur par défaut)

print("--------")

def est_pair(nombre):
    stockage_Resultat = int(0)
    stockage_Resultat = nombre % 2
    resultat_Final = int(0)

    if stockage_Resultat == 0:
        resultat_Final = True
    else:
        resultat_Final = False
    return resultat_Final

#Version bien plus rapide de ce que j'ai fait :
#def est_pair(nombre):
#    return nombre % 2 == 0

def compter_pairs(liste_nombres):
    nombre_Chiffre_Pair = int(0)
    for chaque_Nombre in liste_nombres:
        chaque_Nombre = est_pair(chaque_Nombre)
        if chaque_Nombre == True:
            nombre_Chiffre_Pair = nombre_Chiffre_Pair + 1
    return f"Dans cette liste il y au total {nombre_Chiffre_Pair} chiffre(s) pair(s)."

print(compter_pairs([1, 2, 3, 4, 5, 6, 7, 8]))

print("--------")

#Exercice 1
def doubler_print(nombreA):
    print(nombreA*2)

def doubler_return(nombreB):
    return nombreB*2

resultat_A = doubler_print(5)
resultat_B = doubler_return(5)

print(f"A vaut : {resultat_A}")
print(f"B vaut : {resultat_B}")

print("--------")

#Exercice 2

def calculer_ttc(prix_HT, taux_TVA = 20):
    prix_TTC = prix_HT*(1+taux_TVA/100)
    return prix_TTC

print(calculer_ttc(100))
print(calculer_ttc(100, 5.5))
resultat = calculer_ttc(50)
print(f"Le prix TTC est de {resultat} euros")

print("--------")

#Exercice 3

def est_majeur(age):
    #verification_Age = bool()
    verification_Age = int(0)
    if age >= 18:
        verification_Age = True
    else:
        verification_Age = False
    return verification_Age

#Version plus rapide

#def est_majeur(age):
#    return age >= 18

def compter_majeurs(listes_ages):
    nb_Personne = int(0)
    for une_Personne in listes_ages:
        if est_majeur(une_Personne): # il est inutile de mettre == True ici car la fonction est_majeur renvoie déjà True ou False
            nb_Personne = nb_Personne + 1
    return nb_Personne

print(est_majeur(25))
print(est_majeur(15))

print(compter_majeurs([25, 17, 34, 15, 42, 8, 19]))

print("--------")

#Exercice 4

def calculer_somme(nombres):
    total_Somme = float(0)
    for chaque_Somme in nombres:
        total_Somme = chaque_Somme + total_Somme
    return total_Somme

def calculer_moyenne(nombres):
    total_Moyenne = float(0)
    nb_Nombre = len(nombres)
    total_Moyenne = calculer_somme(nombres)/nb_Nombre
    return total_Moyenne

def trouver_max(nombres):
    chiffre_Max = int(0)
    for chaque_Nombre in nombres:
        if chaque_Nombre > chiffre_Max:
            chiffre_Max = chaque_Nombre
    return chiffre_Max

def analyser_liste(nombres):
    return calculer_somme(nombres), calculer_moyenne(nombres), trouver_max(nombres)


somme, moyenne, maximum = analyser_liste([10, 25, 8, 33, 14])
print(f"Somme : {somme}, Moyenne : {moyenne}, Maximum : {maximum}")

print("--------")

#Exercice 5

eleves = [
    {"nom": "Alice", "note": 14},
    {"nom": "Bob", "note": 8},
    {"nom": "Charlie", "note": 17},
    {"nom": "Diana", "note": 11},
    {"nom": "Eve", "note": 6}
]

def extraire_notes(eleves):
    listes_Notes = []
    for chaque_Note in eleves:
        listes_Notes.append(chaque_Note["note"])
    return listes_Notes

def est_recu(note):
    if note >= 10:
        accepter = True
    else:
        accepter = False
    return accepter

def bilan_classe(eleves):
    nb_Eleves_Recu = int(0)
    for chaque_Note in extraire_notes(eleves):
        if est_recu(chaque_Note) == True:
            nb_Eleves_Recu = nb_Eleves_Recu + 1
    return nb_Eleves_Recu


print(extraire_notes(eleves))
print(bilan_classe(eleves))

print("--------")

#Exercice 6

def doubler(nombre):
    return nombre*2

def doubler_listes(nombres):
    res_Double_Nombre = []
    for chaque_Nombre in nombres:
        res_Double_Nombre.append(doubler(chaque_Nombre))
    return res_Double_Nombre

print(doubler_listes([4,7,2,9]))