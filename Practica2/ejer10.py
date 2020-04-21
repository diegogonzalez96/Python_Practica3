images=['im1','im2','im3']

dicc = {}

for i in images:
    x = int(input("Ingrese coordenada X: "))
    y = int(input("Ingrese coordenada Y: "))
    coord = (x, y)
    if not dicc:
        dicc[i] = coord
    else:
        if coord in dicc.values():
            while coord in dicc.values():
                print("La coordenada ya existe!, ingrese nuevas coordenadas PELELE")
                x = int(input("Ingrese coordenada X: "))
                y = int(input("Ingrese coordenada Y: "))
                coord = (x, y)
            dicc[i] = coord
        else:
            dicc[i] = coord

print(dicc)