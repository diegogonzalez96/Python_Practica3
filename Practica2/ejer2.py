tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

#sort #sorted(l,key=lambda x: x)
list = []

for i in tam:
    name, space, coord = i.partition(" ") #guarda en cada variable su valor correspondiente
    x = int(coord.split(",")[0]) #paso la coordenada x a integer
    y = int(coord.split(",")[1]) #paso la coordenada y a integer
    tupla = (x,y)
    list.extend([tupla])
    list.sort() #list.sort(reverse=True) para ordenar en forma descendente

print(list)

