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

def sum (num):
    x = random.randrange(10)
    y = random.randrange(10)
    res = x + y
    if res == num:
        ok = True
    else:
        ok = False
    return ok

def searchColors(dicc2):
    color = input('Ingrese color: ')
    if color in dicc2.values():
        num = int(input('Ingrese numero para adivinar: '))
        if sum(num):
            print('Adivinaste el numero!')
        else:
            print('No adivinaste, segui participando.')
    else:
        print('El color no existe master.')


palabras = [('grave',['molesto']), ('aguda',['ratón']),('esdrujula',['murciélago'])]

def wordSearc(palabras):
    tuple = palabras[random.randrange(3)]
    word = tuple[1][0]
    option = input('La palabra ' + word + ' es grave, aguda o esdrujula? ')
    answer = tuple[0]
    if option == answer:
        print('Correcto!')
    else:
        print('Incorrecto, la palabra es ' + answer)


searchColors(dicc2)
wordSearc(palabras)