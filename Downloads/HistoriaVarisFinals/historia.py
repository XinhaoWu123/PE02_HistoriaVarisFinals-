import random  # Importem un numero random

random1: int = random.randint(0, 999)  # Generem el numero random que sigui de 0 a 999
print(type(random1))
if random1 < 10:  # Fem un condicional que quan el numero sigui menys de 100 s'anyadin els 0 que calguin 
    num: str = "00" + str(random1)
elif random1 < 100:
    num: str = "0" + str(random1)
else:
    num: str = str(random1)

llista_direccions: tuple[str, str, str] = ("esquerra", "mig", "dreta")  # Guardenm les direccions
personatge: str = input("Introdueix el nom del teu personatge: ").lower().capitalize()  # Fem que l'usuari que introdueixi una informació i la convertim a minúscula i desprès com és un nom majúscula la primera lletra
print(f"Hola {personatge} benvingut al món de la Terra")

cami: str = input("Ets un aventurer en un món màgic i veus tres camins, decideix quin camí vols annar el de la esquerra on veus un camí ple de plantes, el del mig on l'osridad predomina o el de la dreta que sembla un desert (esquerra/mig/dreta)")
cami1: str = cami.lower()

llista: list = []  # Lista per guardar informació
llista.append(cami1)  # Anyadim informació a la llista

while cami1 not in llista_direccions:  # Fem un bucle que si no pasa les opcions l'obliguem a torna a posar-ho
    cami1 = input("Només es pot seleccionar (esquerra/mig/dreta): ").lower()
    if cami1 in llista_direccions:
        llista.append(cami1)

print(f"Veig que has escollit el cami de {cami1} ")

if cami1 == "esquerra":  # Serie d'accions que passa quan esculleix una opció 
    print("Estàs a camí ple de plantes i els arbres et diuen una endevinalla ")
    print("Blanca per dins, verda per fora.\nSi vols que t'ho digui, espera.\n")

    resposta_correcta: str = "pera"

    for comptador in range(3, 0, -1):  # Fem un bucle que tingui 3 oportunitats de contestar amb un for range 3 a 0 cada cop -1
        resposta: str = input("Posa la teva resposta: ").lower()
        if resposta == resposta_correcta:
            print(f"Correcte agafa aquest numero el necesitaras {num}")
            break
        else:
            if comptador - 1 > 0:
                print(f" Incorrecte. Et queden {comptador - 1} intents.")
            else:
                print(" T'has quedat sense intents. Estas mort.")

if cami1 == "mig":
    print("Estas a l'oscuritat total")
    print("Contesta això per sobreviure ")
    print("Sempre va davant teu, però mai el veus.")
    resposta_correcta: str = "futur"

    for comptador in range(3, 0, -1):
        resposta: str = input("Posa la teva resposta: ").lower()
        if resposta == resposta_correcta:
            print(f"Correcte agafa aquest numero el necesitaras {num}")
            break
        else:
            if comptador - 1 > 0:
                print(f" Incorrecte. Et queden {comptador - 1} intents.")
            else:
                print(" T'has quedat sense intents. Estas mort.")

elif cami1 == "dreta":
    print("Estàs al desert i el sol t'enlluerna.")
    print("Resol això per sobreviure:")
    print("Sóc líquid com l'aigua però mai em pots beure. Què sóc?")

    resposta_correcta: str = "mirall"

    for comptador in range(3, 0, -1):
        resposta: str = input("Posa la teva resposta: ").lower()
        if resposta == resposta_correcta:
            print(f"Correcte agafa aquest numero el necesitaras {num}")
            break
        else:
            if comptador - 1 > 0:
                print(f" Incorrecte. Et queden {comptador - 1} intents.")
            else:
                print(" T'has quedat sense intents. Estas mort.")

resposta_final: str = input("""
      ________
     /        \\
    |  LOCKED  |
    | [ 1 2 3 ]|
    |__________|
Posa el numero de la clau : """)

if resposta_final == num:  # Comparem respostes finals
    print("Ho has lograt ")
else:
    print("No ho has aconseguit ")

    

