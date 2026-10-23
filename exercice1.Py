print("Bonjour. Veuillez saisir un nombre entre 1 et 10")
while True:
    try:
        saisi = input()
        saisiVerif = int(saisi)
        if saisiVerif >= 1 and saisiVerif <= 10 :
            saisiCarre = saisiVerif * saisiVerif
            print(saisiCarre)
            break
        else:
            print("Le nombre doit être compris entre 1 et 10, recommencez !")
    except ValueError:
        print("Seulement des chiffres sont autorisés, recommencez !")