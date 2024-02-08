texto = input("Digite a palavra: ")

palindromo = True
tam = len(texto)
invertido = []
validador = 0
for x in range(tam -1, - 1, -1):
    invertido.append(texto[x])

for x in range(tam):
    if invertido[x] != texto[x]:
        palindromo = False

    
if palindromo == True:
    print("O texto é palíndromo")
else:
    print("O texto não é palíndromo")
