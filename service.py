import asyncio

class Service:
    def __init__(self, nom, url):
        self.nom = nom
        self.url = url

    async def ping(self):
        await asyncio.sleep(1)
        return f"{self.nom} : en ligne"

async def main():
        service_a = Service("Lien A", "Url A")
        service_b = Service("Lien B", "Url B")
        service_c = Service("Lien C", "Url C")
        
        affichage = await asyncio.gather(
        service_a.ping(),
        service_b.ping(),
        service_c.ping()
        )
        print(affichage)

asyncio.run(main())























print("-----")

async def saluer(nom, duree):
    await asyncio.sleep(duree)
    return f"Bonjour {nom}"

async def main():
    afficher_Personne = await asyncio.gather(
        saluer("Tristan", 5),
        saluer("Amélie", 2),
        saluer("Ludwig", 3)
    )
    print(afficher_Personne)

asyncio.run(main())