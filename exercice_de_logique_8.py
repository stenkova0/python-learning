def est_adulte(age):
    if age >= 18:
        return True
    else:
        return False

def compter_adultes(listes_ages):
    nb_adulte = int(0)
    for chaque_age in listes_ages:
        if est_adulte(chaque_age) == True:
            nb_adulte = nb_adulte + 1
    return nb_adulte

print(compter_adultes([25, 12, 30, 8, 19]))   # 3