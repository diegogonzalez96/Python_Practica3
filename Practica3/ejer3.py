
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

def userPrint(dicc):
    name = input('Ingrese nombre de usuario a buscar: ')
    if name in dicc.keys():
        print(dicc[name])
    else:
        print('El usuario no existe.')

def usersName(dicc):
    aux = dicc.keys()
    print(aux)

def scoreMax(dicc):
    maximo = max(dicc.items(), key=lambda elem: elem[1][2])
    print('Usuario con puntaje mas alto: ', maximo)
def checkUser(dicc):
    name = input('Ingrese nombre de jugador: ')
    level = int(input('Ingrese nivel: '))
    score = int(input('Ingrese puntaje: '))
    time = int(input('Ingrese tiempo: '))
    if name in dicc.keys():
        if score > dicc[name][2]:
            dicc[name][2] = score
    else:
        list = [name, level, score, time]
        dicc[name] = list
    print(dicc)
    return dicc

def orderScore(dicc):
    diccOrd = sorted(dicc.items(), key=lambda x: x[1][2], reverse=True)[:2]
    print('Ranking 10 mejores puntajes')
    for i in diccOrd:
        print(i[1])



dicc = {}
list = []
diccOrd = []

loadUser(dicc)
userPrint(dicc)
usersName(dicc)
scoreMax(dicc)
checkUser(dicc)
orderScore(dicc)

