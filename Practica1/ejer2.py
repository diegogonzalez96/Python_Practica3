print("ingrese texto: ")
texto = input()

print("ingrese palabra a buscar: ")
busqueda = input()

palabras_texto = texto.split(' ')

print(palabras_texto)

#palabras_busqueda = [s for s in palabras_texto if busqueda in s] //sin la modificacion

palabras_busqueda = [s for s in palabras_texto if busqueda.upper() in s.upper()]
print("se encontraron ", len(palabras_busqueda))
