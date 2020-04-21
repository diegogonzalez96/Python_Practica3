word = input("Ingrese una palabra:")

dicc = {}
list = []

def num_primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

for i in word:
    if i in dicc: #comprueba que la clave i exista en el diccionario
        dicc[i] = dicc[i]+1 #si existe aumentamos en 1 el valor
    else:
        dicc[i] = 1

for i in dicc:
    num = dicc[i]
    if num_primo(num):
        list.append(i)
    print("La letra ", i, "aparece: ", num, " veces")

print("Por tanto las letras ", end="") #end="" para que no haga ningun salto de linea
print(list, end="")
print(" son letras que aparecen un numero de primo veces")








