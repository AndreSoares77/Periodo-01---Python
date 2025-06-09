lista = [50, 30, 60, 20, 15, 5, 40, 32, 10]

for j in range(len(lista)):
    for i in range(j, len(lista)):
        if i == j: 
            pos_menor = j
        elif lista[pos_menor] > lista[i]:
            pos_menor = i
            
    lista[j], lista[pos_menor] = lista[pos_menor], lista[j]

print(lista)