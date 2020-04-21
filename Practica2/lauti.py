import random

palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}
ahorcado = [' O ', '/|\\','/ \\']


def pideDato():
    aux = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
    while(aux>3) or (aux<1):
        aux = int(input('El número ingresado es incorrecto. Vuelva a ingresarlo: '))
    return aux

def buscaLetra(letra, cant_letras_adivinadas):
    for pos in range(len(pal)):
        if pal[pos]==letra:
            palabra_separada[pos]=letra
            cant_letras_adivinadas=cant_letras_adivinadas+1
    return palabra_separada, cant_letras_adivinadas

def resultado(cant_letras_adivinadas):
    if cant_letras_adivinadas == len(pal):
        print ('Ganaste!')
        sigue=False
    else:
        sigue=True
    return sigue

def perdiste(cant_partes_cuerpo):
    for x in range (cant_partes_cuerpo):
        print (ahorcado[x])
    if cant_partes_cuerpo == 3:
        print ('Perdiste!. La palabra era: ',pal)
        sigue=False
    else:
        sigue=True
    return sigue


tema=pideDato()
pal = palabras[tema][random.randrange(len(palabras[tema]))]

palabra_separada = []
for i in pal:
    palabra_separada.append(['_ '])


print ('- ' *len(pal))

cant_letras_adivinadas=0
cant_partes_cuerpo = 0

sigue= True
while sigue:
    letra = input ('Ingresa una letra: ').lower()
    if letra in pal:
        palabra_imprime, cant_letras_adivinadas=buscaLetra(letra, cant_letras_adivinadas)
        palabra_imprime = ''
        for j in palabra_separada:
            palabra_imprime = palabra_imprime + j[0]
        print (palabra_imprime)
        sigue=resultado(cant_letras_adivinadas)
    else:
        cant_partes_cuerpo = cant_partes_cuerpo + 1
        sigue= perdiste(cant_partes_cuerpo)