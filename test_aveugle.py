def encadrer(fonction):
    def nouvelle_fonction(*args):
        print("***")
        fonction(*args)
        print("***")
    return nouvelle_fonction

@encadrer
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()

@encadrer
def dire(message):
    print(message)

dire("Salut")
print("-----")
# ----------------------------

import time

def timer_avant(fonction):
    def nouvelle_fonction(*args):
        debut = time.time()
        fonction(*args)
        fin = time.time()
        print(fin-debut)
    return nouvelle_fonction

@timer_avant
def calculer_somme(n):
    total = 0
    for i in range(n):
        total = total + i
    return total

calculer_somme(10000000)