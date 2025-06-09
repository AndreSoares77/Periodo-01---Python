cont_peso = 0
cont_combustivel = 0
cont_altitude = 0

while True:
    valores = input().split()
    if int(valores[0]) < 0:
        print('dado inconsistente. peso negativo.')
        break
    else:
        cont_peso += 1
    if int(valores[1]) < 0:
        print('dado inconsistente. combustível negativo.')
        break
    else:
        cont_combustivel += 1
    if int(valores[2]) < 0:
        print('dado inconsistente. altitude negativa.')
        break
    else:
        cont_altitude += 1

print(f'peso: {cont_peso}')
print(f'combustível: {cont_combustivel}')
print(f'altitude: {cont_altitude}')