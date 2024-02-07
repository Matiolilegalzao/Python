lista = []
tam = int(input("Informe o tamanho da lista: "))
maior = 0
for x in range(tam):
    num = int(input(f"Informe o número {x + 1}: "))
    lista.append(num)
    if maior < num:
        maior = num

menor = maior
for i in range(tam):
    if menor > lista[i]:
        menor = lista[i]

print("Maior número:", maior)
print("Menor número: ", menor)
