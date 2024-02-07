lista = []
tam = int(input("Informe o tamanho da lista: "))

for i in range(1, tam + 1):
    n = int(input(f"Informe o número [{i}]: "))
    lista.append(n)

print(lista)