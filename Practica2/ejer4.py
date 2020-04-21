preguntas = [['¿Buenos Aires limita con Santiago del Estero?', 'no'], ['¿Jujuy limita con Bolivia?', 'si'], ['¿San Juan limita con Misiones?', 'no']]

import random


b = len(preguntas)-1
score = 0

while preguntas:
    opcion = random.randint(0, b)
    print("Toco pregunta numero :", opcion)
    print(preguntas[opcion][0])
    resp = input()
    if resp.lower() == preguntas[opcion][1]:
        score +=1
    elif resp.lower() == preguntas[opcion][1]:
        score +=1
    preguntas.pop(opcion)
    b = len(preguntas)-1

print("Puntaje final: ", score)

