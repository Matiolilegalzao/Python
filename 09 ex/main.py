entradas = int(input("Quantas strings você vai inserir?: "))
tempString = []
lista = []

for x in range(entradas):
    tempString = input(f"Insira a string número {x+1}: ")
    lista.append(tempString)
    if len(tempString) <= 5:
        lista.pop()

print(lista)