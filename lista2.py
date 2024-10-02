jegy = [1 , 2 , 3 , 4 , 5]
oszt = ['9/ny' , '10/b' , '11/c' , '12/b haladó' , '1/13b' , '2/14b']
nev = ['Ákos' , 'Dénes' , 'Laci' , 'Levente' , 'Nelli' , 'Regina']

jegy[0] = jegy[2]
print(jegy)

oszt[1] = oszt[2]
print(oszt)
#nev[-1] = nev[2]
nev[len(nev)-1] = nev[2]
print(nev)