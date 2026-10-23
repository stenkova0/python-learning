personnes = [
    {"nom": "Alice", "age": 28, "poste": "dev"},
    {"nom": "Bob", "age": 35, "poste": "manager"},
    {"nom": "Charlie", "age": 22, "poste": "dev"},
    {"nom": "Diana", "age": 41, "poste": "manager"},
    {"nom": "Eve", "age": 30, "poste": "dev"}
]

def analyser_equipe(personnes):
    total_Age = int(0)
    age_Moyen = int(0)

    comparateur_age = int(0)
    personne_plus_age = ""

    nb_devs = int(0)

    taille_liste_Personne = len(personnes)
    for chaque_Personne in personnes:
        total_Age = chaque_Personne["age"] + total_Age
        if chaque_Personne["age"] > comparateur_age:
            comparateur_age = chaque_Personne["age"]
            personne_plus_age = chaque_Personne["nom"]
        if chaque_Personne["poste"] == "dev":
            nb_devs = nb_devs + 1

    age_Moyen = total_Age / taille_liste_Personne

    return age_Moyen, personne_plus_age, nb_devs

def filtrer_par_poste(personnes, poste = "dev"):

    liste_globale = []

    for chaque_Personne in personnes:
        if chaque_Personne["poste"] == poste:
            liste_globale.append(chaque_Personne["nom"])
    return liste_globale

def age_moyen_par_poste(personnes, poste):
    total_Age = int(0)
    moyenne_Age = int(0)

    liste_globale = []

    for chaque_Personne in personnes:
        if chaque_Personne["poste"] == poste:
            total_Age = total_Age + chaque_Personne["age"]
            liste_globale.append(total_Age)

    taille_liste = len(liste_globale)
    moyenne_Age = total_Age / taille_liste
    return moyenne_Age



print (analyser_equipe(personnes))
print(filtrer_par_poste(personnes, "dev"))
print(filtrer_par_poste(personnes, "manager"))
print(age_moyen_par_poste(personnes, "dev"))
print(age_moyen_par_poste(personnes, "manager"))