num = int(input("Informe um número: "))
divisores = []
for x in range(1, num + 1):
    if num % x == 0:
        divisores.append(x)
print(f"Divisores de {num}:", divisores)