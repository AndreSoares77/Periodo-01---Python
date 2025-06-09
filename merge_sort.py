lista01 = [10, 20, 30, 40, 55]
lista02 = [15, 25, 35]

i = 0
j = 0
lista_nova = []

while True:
    if i == len(lista01):
        for l in range(j, len(lista02)):
            lista_nova.append(lista02[l])
        break

    if j == len(lista02):
        for l in range(i, len(lista01)):
            lista_nova.append(lista01[l])
        break

    if lista01[i] <= lista02[j]: 
        lista_nova.append(lista01[i])
        i += 1
    else:
        lista_nova.append(lista02[j])
        j += 1

print(lista_nova)