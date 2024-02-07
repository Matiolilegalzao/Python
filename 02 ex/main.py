lista = []
listaPar = []
tam = int(input("Informe o tamanho da lista: "))

for i in range(tam):
    n = int(input(f"Informe o número [{i + 1}]: "))
    lista.append(n)

for i in range(tam):
    if lista[i] % 2 == 0:
        listaPar.append(lista[i])

print(f"Lista 1: {lista}")
print(f"Lista 2: {listaPar}")

