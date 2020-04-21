print("Ingrese palabra: ")
word1 = input()

word2 = word1[::-1] #invierte la cadena de string

if word1.lower() == word2.lower():
    print("La palabra es un palindromo.")
else:
    print("La palabra no es un palindromo.")