"""
7. Gipsz Jakab
A feladat: megcserélni egy névben a keresztnevet és a vezetéknevet, és az eredményt egy másik sztringben előállítani.
"""


beker = input()


szet = beker.split()

forditott = szet[-1] + " " + szet[0]

print("|" + forditott + "|")

#kereszt
#vezetek
