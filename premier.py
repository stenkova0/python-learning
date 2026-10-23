#Afficher un message
age = 31
print(f"J'ai {age} ans ")

#Utilisation de la fonction type() sur des variables
un_entier = 10
un_decimal = 5.5
un_texte = "Bonjour !"
un_booleen = True

print(type(un_entier))
print(type(un_decimal))
print(type(un_texte))
print(type(un_booleen))

#Différents calculs
chiffre_entier1 = 10
chiffre_decimal1 = 15.5
chiffre_entier2 = 20
chiffre_decimal2 = 26.2

print(chiffre_entier1 + chiffre_decimal1)
print(chiffre_decimal2 - chiffre_entier2)
print(chiffre_entier1 * chiffre_entier2)
print(chiffre_decimal2 / chiffre_decimal1)

#Division pleine
division = 10//3
print(division)

#Division négative et reste
division_negative = -10//3
division_negative_reste = -10%3
print(division_negative)
print(division_negative_reste)

#Puissance
puissance = 2**3
print(puissance)

#Saisi d'une réponse
print("Quel âge avez vous ?")
age = input() #Par défaut un input() transforme la variable en str
doubleAge = int(age) * 2
print(f"Vous avez {doubleAge} ans !")

#Saisi de l'âge et déterminer si mineur ou majeur
print("Quel âge avez vous ?")

while True:
    try:
        age = input()
        ageVerification = int(age)
        if ageVerification <= 17:
            print("Vous êtes mineur !")
            break
        else:
            print("Vous êtes majeur !")
            break
    except ValueError:
        print("Une erreur est arrivée")

#else ne vérifie rien, elif lui vérifie vérifie une nouvelle condition. Ici elif n'est donc pas nécessaire puisque si la personne n'a pas 17 ans elle en a forcément au moins 18