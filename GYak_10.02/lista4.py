jegy = [1 , 2 , 3 , 4 , 5]
oszt = ['9/ny' , '10/b' , '11/c' , '12/b haladó' , '1/13b' , '2/14b']
nev = ['Ákos' , 'Dénes' , 'Laci' , 'Levente' , 'Nelli' , 'Regina']

del jegy[0]
print(jegy)

#oszt.pop(-1)
oszt.pop(len(oszt)-1)
print(oszt)

nev.remove('Ákos')
print(nev)
