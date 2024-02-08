print("Informe números, insira 'fim' para terminar")
lista = []
x = 0
while True:
    lista.append((input()))
    if lista[-1] == "fim":
        lista.pop()
        break
    lista[-1] = int(lista[-1])
    if lista[-1] % 2 != 0:
        lista.pop()


print("Números pares:", lista)