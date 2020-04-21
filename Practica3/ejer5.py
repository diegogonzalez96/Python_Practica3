import random

colores = ['azul','amarillo','rojo','blanco','negro']

coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]

dicc1 = {}
for i in coordenadas:
    dicc1[i] = random.choice(colores)
print(dicc1)

dicc2 = {}
for i in coordenadas:
    dicc2[i] = random.choice(colores)
    colores.remove(dicc2[i])
print(dicc2)