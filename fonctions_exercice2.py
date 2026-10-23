def doubler(nombre):
    return nombre*2

def doubler_listes(nombres):
    res_Double_Nombre = []
    for chaque_Nombre in nombres:
        res_Double_Nombre.append(doubler(chaque_Nombre))
    return res_Double_Nombre

def est_pair(nombre):
    return nombre % 2 == 0

def filtrer_pairs(nombres):
    liste_Nombre_Pair = []
    for chaque_Nombre in nombres:
        if est_pair(chaque_Nombre) == True:
            liste_Nombre_Pair.append(chaque_Nombre)
    return liste_Nombre_Pair

def appliquer(nombres, fonction):
    for chaque_Nombre in nombres:
        

print(est_pair(2))
print(est_pair(3))
print(doubler_listes([4,7,2,9]))
print(filtrer_pairs([4,7,2,9]))
