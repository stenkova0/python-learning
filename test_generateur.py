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