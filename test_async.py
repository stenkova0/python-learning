#Synchrone
import time

#def tache_lente(nom, duree):
 #   print(f"{nom} commence...")
  #  time.sleep(duree)
   # print(f"{nom} terminée après {duree}s")

#debut = time.time()
#tache_lente("Tâche A", 2)
#tache_lente("Tâche B", 2)
#tache_lente("Tâche C", 2)
#fin = time.time()
#print(f"Total : {fin - debut:.1f}s")

#Asynchrone

import asyncio

async def tache_lente(nom, duree):
    print(f"{nom} commence...")
    await asyncio.sleep(duree)
    print(f"{nom} terminée après {duree}s")

async def main():
    debut = asyncio.get_event_loop().time()
    await asyncio.gather(
        tache_lente("Tâche A", 2),
        tache_lente("Tâche B", 2),
        tache_lente("Tâche C", 2)
    )
    fin = asyncio.get_event_loop().time()
    print(f"Total : {fin - debut:.1f}s")

asyncio.run(main())
print("-----")

# T2

async def calculer(nom, duree):
    print(f"{nom} en cours...")
    await asyncio.sleep(duree)
    return duree * 10

async def main():
    resultats = await asyncio.gather(
        calculer("A", 1),
        calculer("B", 2),
        calculer("C", 1)
    )
    print(resultats)

asyncio.run(main())
print("-----")

# T3

async def appel_api(nom, duree):
    print(f"{nom} en cours...")
    await asyncio.sleep(duree)
    return {"api": nom, "status": "ok"}

async def main_api():
    debut_api = asyncio.get_event_loop().time()
    affichage = await asyncio.gather(
        appel_api("Api A", 5),
        appel_api("Api_B", 2),
        appel_api("Api_C", 3)
    )
    print(affichage)
    fin_api = asyncio.get_event_loop().time()
    print(f"Total : {fin_api - debut_api:.1f}s")

asyncio.run(main_api())