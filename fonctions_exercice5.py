employes = [
    {"nom": "Alice", "salaire": 2800},
    {"nom": "Bob", "salaire": 3500},
    {"nom": "Charlie", "salaire": 2200},
    {"nom": "Diana", "salaire": 4100},
    {"nom": "Eve", "salaire": 1900}
]

def est_senior(salaire):
    return salaire > 3000

def bilan_equipe(employes):
    liste_Noms_Employes = []
    nb_Seniors = int(0)
    nb_Employe = len(employes)
    salaire_moyen = float(0)
    total_salaire = float(0)

    for chaque_Employe in employes:
        if est_senior(chaque_Employe["salaire"]) == True:
            liste_Noms_Employes.append(chaque_Employe["nom"])
            nb_Seniors = nb_Seniors + 1

        total_salaire = total_salaire + chaque_Employe["salaire"] 

    salaire_moyen = total_salaire / nb_Employe
    return liste_Noms_Employes, nb_Seniors, salaire_moyen

print(bilan_equipe(employes))