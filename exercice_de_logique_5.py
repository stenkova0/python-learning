def convertir_temps(secondes):
    heure_total = int(0)
    minutes_total = int(0)
    secondes_total = int(0)

    minutes_total = secondes // 60
    secondes_total = secondes % 60

    heure_total = minutes_total // 60
    minutes_restantes = minutes_total % 60

    return heure_total, minutes_restantes, secondes_total

print(convertir_temps(3661))   # (1, 1, 1) → 1h 1min 1s
print(convertir_temps(7200))   # (2, 0, 0) → 2h 0min 0s
print(convertir_temps(125))    # (0, 2, 5) → 0h 2min 5s