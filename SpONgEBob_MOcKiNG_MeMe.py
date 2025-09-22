"""
Írj programot, amelyik a beírt sorból olyan sztringet állít elő, amelyben VÉletLEnszErŰeN VÁLtAkoZnAK
 a kis- és nagybetűk! Használd az előadáson tanult sztringműveleteket!

Pythonban véletlenszámot a random modul (import random) egyik függvényével tudsz létrehozni.
 Ennek neve: random.randint(). Paramétere egy alsó és egy felső határ; random.randint(0, 1) véletlenszerűen 0-t vagy 1-et ad.

"""
txt = input()
import random

szoveg = ""

for betu in txt:
    if random.randint(0,1) == 1:
        szoveg = szoveg + betu.upper()
    else:
        szoveg = szoveg + betu.lower()


print(szoveg)








txt = input()

egyezik = True

for i in range(0,int(len(txt)/2)):
    if txt[i] != txt[len(txt)-1-i]:
        egyezik = False
        break

if egyezik:
    print("polindrom")
else:
    print("nem polindrom")


