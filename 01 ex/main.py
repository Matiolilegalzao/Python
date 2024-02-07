num = int(input("Informe um número para verificar se ele é primo:", ))
contador = 0
for x in range(1, num + 1):
    if num % x == 0:
        contador+= 1
if contador == 2:
    print("Primo")
else:
    print("Não é primo")