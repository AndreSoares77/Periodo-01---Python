lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numero = 56

lista.append(numero)
i = len(lista)-1

while True:
    if numero > lista[i-1] or i == 0: break
    lista[i-1],lista[i] = lista[i],lista[i-1]
    i -= 1

print(lista)