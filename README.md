# fun fact a stringekről
_*LSD -->*_ C, C++

```python

ord("A")  # 65 a kódja

chr(65)   # "A" betű

chr(ord("A") + 3)  # D mert a,b,c,d
```

### feladatok:
```python
"""
4. Palindrom II.
Írj programot, amelyik egy mondatról eldönti, hogy palindrom-e.
Közismert magyar nyelvű palindrom mondat az „Indul a görög aludni.
” Ez abban különbözik az előző feladattól, hogy most
a szóközöket és az írásjeleket ki kell szűrnöd, vagyis
csak a betűket kell megtartani, és úgy kell vizsgálni
a sztringet. És persze figyelni arra is, hogy a kisbetűk
és a nagybetűk nem különböznek.
"""
bekeres = input("Kérek egy szöveget:\t")
bekeres = bekeres.lower()

palindrom = ""
irasjelek_nelkul = ''
meddig = len(bekeres)-1
irasjelek = [" ", ".", ":", "!", "?"]


index = 0
while index <= meddig:
    if bekeres[index] not in irasjelek:
        irasjelek_nelkul += bekeres[index]
    index+=1

print(irasjelek_nelkul)


while meddig >= 0:
    if bekeres[meddig] not in irasjelek:
        palindrom += bekeres[meddig]
    meddig-=1

    
if irasjelek_nelkul == palindrom:
    print("ez a mondat: '"+ bekeres + "' palindrom!")
else:
    print("ez a mondat: '"+ bekeres + "' NEM palindrom!")
```
