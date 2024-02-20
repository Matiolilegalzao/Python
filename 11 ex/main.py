listastr = ["maça", "banana", "laranja", "carambola"]
def stringLonga(lista):
    longa = max(lista, key=len)
    return longa

print(stringLonga(listastr))

