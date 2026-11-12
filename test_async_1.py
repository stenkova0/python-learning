import asyncio

class Serveur():
    def __init__(self, nom):
        self.nom = nom

    async def verifier(self):
        await asyncio.sleep(2)
        return f"{self.nom} : OK"

async def main():
    serveur_A = Serveur("Serveur A")
    serveur_B = Serveur("Serveur B")
    serveur_C = Serveur("Serveur C")
    resultat = await asyncio.gather(
        serveur_A.verifier(),
        serveur_B.verifier(),
        serveur_C.verifier()
    )
    print(resultat)

asyncio.run(main())