print("Bonjour dans le convertisseur de température. Veuillez sélectionner si vous voulez convertir du Celsisus vers Fahrenheit ou l'inverse.\n1 - Celsius vers Fahrenheit\n2 - Fahrenheit vers Celsius")

while True:
    try:
        choix = input()
        choixVerification = int(choix)
        if choixVerification == 1:
            print("Vous avez choisi Celsius vers Fahrenheit. Indiquer la valeur :")
            while True:
                try:
                    temperature_en_Celsius = input()
                    temperature_en_Celsius_Verification = float(temperature_en_Celsius)
                    conversion_vers_Fahrenheit = temperature_en_Celsius_Verification * 9/5 + 32
                    print(f"La température en Fahrenheit est de {conversion_vers_Fahrenheit}")
                    break
                except ValueError:
                    print("Seuls les chiffres sont autorisés. Recommencez !")
            break
        elif choixVerification == 2:
            print("Vous avez choisi Fahrenheit vers Celsius. Indiquer la valeur :")
            while True:
                try:
                    temperature_en_Fahrenheit = input()
                    temperature_en_Fahrenheit_Verification = float(temperature_en_Fahrenheit)
                    conversion_vers_Celsius = (temperature_en_Fahrenheit_Verification - 32) * 5/9
                    print(f"La température en Celsius est de : {conversion_vers_Celsius}")
                    break
                except ValueError:
                    print("Seuls les chiffres sont autorisés. Recommencez !")
            break
        else:
            print("La valeur que vous avez saisi ne correspond pas. Veuillez reommencez !")
    except ValueError:
        print("Il y a eu une erreur dans la saisie, recommencez !")
