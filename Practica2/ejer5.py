print("Menú de opciones para la lista de números a ingresar:")
print("1: ingresar números")
print("2: ordenar números")
print("3: calcular el máximo")
print("4: calcular el mínimo")
print("5: calcular el promedio")
print("0: para terminar")

list = []
print("Ingresa opcion a elegir: ")
option = int(input())
while option != 0:
    if option == 1:
        print("Ingrese numero")
        list.append(int(input()))
    elif option == 2:
        list.sort()
        print("Lista ordenada: ")
        print(list)
    elif option == 3:
        print("Maximo: ", max(list))
    elif option == 4:
        print("Minimo: ", min(list))
    elif option == 5:
        prom = sum(list)/len(list)
        round(prom, 2)
        print("Promedio: ", prom)

    print("Menú de opciones para la lista de números a ingresar:")
    print("1: ingresar números")
    print("2: ordenar números")
    print("3: calcular el máximo")
    print("4: calcular el mínimo")
    print("5: calcular el promedio")
    print("0: para terminar")

    print("Ingresa opcion a elegir: ")
    option = int(input())

if not list:
    print("La lista esta vacia.")




