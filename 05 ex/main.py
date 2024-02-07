lista1 = []
lista2 = []
lista3 = []
tam1 = int(input("Informe o tamanho da lista 1: "))

for x in range(tam1):
    num = int(input(f"Informe o número {x + 1}: "))
    lista1.append(num)

tam2 = int(input("Informe o tamanho da lista 2: "))

for x in range(tam2):
    num = int(input(f"Informe o número {x + 1}: "))
    lista2.append(num)

set1 = set(lista1)
set2 = set(lista2)

lista3 = list(set1.intersection(set2))

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)