frase = "Si trabajás mucho CON computadoras, eventualmente encontrarás que te \n" \
        "gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una \n" \
        "búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y \n" \
        "reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras \n" \
        "escribir alguna pequeña base de datos personalizada, o una aplicación especializada \n" \
        "con interfaz gráfica, o UN juego simple."

print(frase)
print()
frase = frase.split(" ") #creo una lista de string separados por espacio

lista_nue = []
#usar funcion replace
print(frase)
print()
for i in frase:
    if i.lower() not in lista_nue:
        lista_nue.append(i.lower()) #agrega el elemento i al final de la lista y convierte ese elemento a minuscula

print(lista_nue)
print()
frase_nue = " ".join(lista_nue)

print(frase_nue)
