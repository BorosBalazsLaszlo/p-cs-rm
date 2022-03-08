# feladat.py

# 1. feladat
# Írjon függvényt ebetuk_szama néven
# A függvény határozza meg a paraméterben kapott stringben hány "e" betű van!

def ebetuk_szama(szo:str) -> int:
    db = 0
    for betu in szo:
        if betu == 'e':
            db = db + 1
    return db

# 2. feladat
# Írjon függvényt szavak_szama néven
# Határozza meg, hogy a paramérerben kapott mondatban hány darab szó
def szavak_szama(szavak:str)-> int:
    szavak = szavak.split()
    print(szavak)
    return len(szavak)



# 3. feladat
# Írjon függvényt harom_betus_szavak néven
# A föggvény paraméterben egy mondatot kap.
# A függvyén határozza meg a mondat lévő három betűs szavakat
# A karakterláncban csak betűk és szóközök vannak, írásjelek nélkül
def harom_betus_szavak(mondat:str)->int:
    db = 0
    mondat = mondat.split()
    for szo in mondat:
        if len(szo) == 3:
            db = db + 1
    return db

# 4. feladat
# Írjon függvényt legrovidebb_szo néven
# A függvény határzza meg a legrövidebb szó hosszát a paraméterben kapott mondatba.
def legrovidebb_szo(mondat:str)->int:
    if len(mondat) == 0:
        return 0
    szavak = mondat.split()
    #első szó hossza
    min = len(szavak[0])
    #vesszük az összes többi szót
    for index in range(1, len(szavak)):
        if len(szavak[index]) < min:
            min = len(szavak[index])
            #index-edik szó hossza
    return min