soma = 0
lista_numeros = list()

while True:
    numero = input()
    if numero == 'fim': break
    numero = int(numero)
    soma += numero
    lista_numeros.append(numero)

media = soma/len(lista_numeros)

for i in range(len(lista_numeros)):
    if lista_numeros[i] < media:
        print(f'{i+1} {lista_numeros[i]}')