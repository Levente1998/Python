lst = [21, 32, 13, 44, 75]
x = int(input('Hanyadik elemet módosítsam a listában? Írj be kérlek egy számot :  '))-1
y = int(input('Írj be kérlek egy számot :  '))



if x >= len(lst) or x < 0:
    print('Nagy számot adtál meg.')

else:
    lst[x] = y
    print(lst)

lst.pop(len(lst)-1)
print(lst)

print(len(lst))

for x in lst:
    print(x)