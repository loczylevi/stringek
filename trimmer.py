"""
6. Trimmer
Gyakori feladat, hogy egy sztring elejéről és végéről el kell távolítani a szóközöket.
Ezt a függvényt gyakran trim-nek vagy strip-nek szokták hívni. Pythonban is van ilyen: " helló világ ".strip() értéke "helló világ".

A feladatod megírni ezt az algoritmust, hogy megértsd a működését! Írj olyan programot,
ami kér egy szöveget, és eltávolítja annak elejéről és végéről a szóközöket. Írd ki utána idézőjelek között a vágott sztringet!

Ha elkészültél, ellenőrizd, működik-e a programod olyan sztringre, ami csak szóközt tartalmaz,
vagy esetleg eleve teljesen üres! Ha nem, javítsd ki!
"""



beker = input()

formazott = ""

index = 0
hossz = len(beker)-1
for betu in beker:
    if index != 0 or index != len(beker)-1:
          pass
    else:
          formazott += betu
    index+= 1




print(f"'{formazott}'")