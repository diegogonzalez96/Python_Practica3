tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

l_lower = [] #menor
l_greater = [] #mayor


print("ingrese numero:")
num = int(input())

for i in tam:
    name, space, coord = i.partition(" ") #guarda en cada variable su valor correspondiente
    x = int(coord.split(",")[0]) #paso la coordenada x a integer
    y = int(coord.split(",")[1]) #paso la coordenada y a integer
    tupla = (x,y)
    if x < num:
        l_greater.extend([name, tupla])
    else:
        l_lower.extend([name, tupla])

print(l_lower)
print(l_greater)
