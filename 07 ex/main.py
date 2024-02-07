lista = [10, 20]

def mediaVetor(lista):
    soma = 0
    for x in range(len(lista)):
        soma += lista[x]

    return(soma / len(lista))

print(mediaVetor(lista))