print()

#Vraag 1.3
prijzen = {
    "aardbei":int("3"),
    "vanille":int("4"),
    "chocolade":int("5")
}
aanbieding = prijzen["aardbei"]*0.8
print("vraag 1.3: ", aanbieding)

#Vraag 1.4
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
print("vraag 1.4: ", reclame_tekst)

#vraag 1.5
reclame_tekst2 = reclame_tekst[:62]
print("vraag 1.5: ", reclame_tekst2)

#vraag 1.6
reclame_tekst3 = reclame_tekst2.upper()
print ("vraag 1.6: ", reclame_tekst3)

#vraag 1.7
reclame_tekst4 = reclame_tekst3.split(" ")
print ("vraag 1.7: ", reclame_tekst4)


#vraag 1.8
print("vraag 1.8: ")
for el in reclame_tekst4:
    print(el)

#vraag 1.9
print()
print("vraag 1.9: ")
for el in reclame_tekst4:
    print(el.lower())

#vraag 1.10
print()
print("vraag 1.10: ")
for el in reclame_tekst4:
    if len(el)>4:
        print(el)
    else:
        print(el.lower())