def desloca(lista, origem, destino):
    while origem != destino:
        lista[origem],lista[origem+1] = lista[origem+1],lista[origem]
        origem += 1
    return lista

l1 = [0,1,2,3,4,5,6,7,8,9]
print(desloca(l1,8,9))

