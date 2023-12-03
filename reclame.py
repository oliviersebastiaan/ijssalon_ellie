#Les 8 Vraag 12:
from algemene_functies import mijn_functie_2

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

#Les 8 Vraag 5:
def aanbieding_1(smaak, prijs, korting):
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-prijs*korting} euro."
print(aanbieding_1("Aarbei", 4, 0.1))

#Les 8 Vraag 6:
def inkomsten_totaal(inkomsten):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    return totaal

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))

#Les 8 Vraag 7:
def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

#Les 8 Vraag 8:
def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

#Les 8 Vraag 9:
def gemiddelde(mijn_lijst):
    totaal = 0
    for nr in mijn_lijst:
        totaal += nr
    bedrag = totaal/7
    return bedrag

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

#Les 8 Vraag 10:
def gemiddelde(mijn_lijst):
    totaal = 0
    for nr in mijn_lijst:
        totaal += nr
    bedrag = totaal/7
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

#Les 8 Vraag 11:
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

print(meervoudig([10,5,3,2,1,2,9]))