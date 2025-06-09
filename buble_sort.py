lista = [10, 30, 60, 20, 15, 5, 40, 32, 50]

for j in range(len(lista)):
    
    for i in range(len(lista)-j):
        if i == 0: 
            pos_maior = 0
        elif lista[pos_maior] < lista[i]:
            pos_maior = i

    lista[pos_maior], lista[i] = lista[i], lista[pos_maior]

print(lista)