def compter_jusqua(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1

for nombre in compter_jusqua(5):
    print(nombre)

print("-----")

def compter_pairs_jusqua(n):
    i = 1
    while i <= n:
        i = i + 1
        if i % 2 == 0:
            yield i

for nombre in compter_pairs_jusqua(10):
    print(nombre)

print("-----")

def fibonacci(n):
    a = 0
    b = 1
    compteur = 0
    while compteur < n:
        yield a
        a, b = b, a + b
        compteur = compteur + 1

for nombre in fibonacci(8):
    print(nombre)


def etoiles(fonction):
    def nouvelle_fonction(*args):
        print("***")
        fonction(*args)
        print("***")
    return nouvelle_fonction

@etoiles
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()

@etoiles
def dire(message):
    print(message)

dire("Salut")