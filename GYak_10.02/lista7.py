'''Hozz létre egy programot, mely
bekéri, hogy hány elemet szeretnél megadni, majd
létrehoz egy listát és
feltölti a iistát a felhasználó átal megadott értékekkel
A lista elemeinek sorrendje fordítottja legyen a felhasználó által megadott értékek sorrendjének
'''

hossz = int(input('Írd be a lista hosszát: '))

lista = []

for i in range(hossz):
   szam = int(input('Írd be egy értéket: '))
   lista.append(szam)

lista.reverse()
print(lista)
