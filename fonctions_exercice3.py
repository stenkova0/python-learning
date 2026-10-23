def est_chaud(temperatures):
    return temperatures >= 25

def jours_chauds(temperatures):
    liste_Jours_Chauds = []
    total_Nb_Jours_Chauds = int (0)
    for chaque_Temperatures in temperatures:
        if est_chaud(chaque_Temperatures) == True:
            liste_Jours_Chauds.append(chaque_Temperatures)
            total_Nb_Jours_Chauds = total_Nb_Jours_Chauds + 1
    return liste_Jours_Chauds, total_Nb_Jours_Chauds

jours = [
    {"jour": "lundi", "temp": 28},
    {"jour": "mardi", "temp": 15},
    {"jour": "mercredi", "temp": 32},
    {"jour": "jeudi", "temp": 19}
]

def jours_chauds_noms(jours):
    liste_jours_chauds = []
    for temperatures_chaque_jour in jours:
        if est_chaud(temperatures_chaque_jour["temp"]) == True:
            liste_jours_chauds.append(temperatures_chaque_jour)
    return liste_jours_chauds

print(jours_chauds_noms(jours))