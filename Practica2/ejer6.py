print("Ingrese primer numero: ")
a = int(input())
print("Ingrese segundo numero: ")
b = int(input())

print("Menú de opciones: ")
print("1: Suma: +")
print("2: Resta: -")
print("3: Multiplicacion: *")
print("4: Division: /")

print("Ingrese opcion a elegir: ")
option = int(input())

if option == 1:
    c = a+b
    print("La suma es: ", c)
elif option == 2:
    c = a-b
    print("La resta es: ", c)
elif option == 3:
    c = a*b
    print("La multiplicacion es: ", c)
elif option == 4:
    if b > 0:
        c = float(a/b)
        round(c)
        print("La division es: ", c)
    else:
        print("No se puede dividir por cero")



