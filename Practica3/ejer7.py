def loadUser(dicc):
    name = input('Ingrese nombre de jugador: ')
    if name != 'zzz':
        level = int(input('Ingrese nivel: '))
        score = int(input('Ingrese puntaje: '))
        time = int(input('Ingrese tiempo: '))

    while name != 'zzz':
        list = [name, level, score, time]
        dicc[name] = list
        name = input('Ingrese nombre de jugador: ')
        if name != 'zzz':
            level = int(input('Ingrese nivel: '))
            score = int(input('Ingrese puntaje: '))
            time = int(input('Ingrese tiempo: '))
    return dicc

def orderScore(dicc):
    order = sorted(dicc.items(), key=lambda x: x[1][2], reverse=True)
    print(order)

def orderName(dicc):
    order = sorted(dicc.items(), key=lambda x: x[1][0])
    print(order)

def orderLevel(dicc):
    order = sorted(dicc.items(), key=lambda x: x[1][1], reverse=True)
    print(order)

dicc = {}
loadUser(dicc)
orderScore(dicc)
orderName(dicc)
orderLevel(dicc)