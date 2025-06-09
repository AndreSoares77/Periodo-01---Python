def quantidade_usuarios(cadastro):
    if cadastro.get(9999) != None:
        del cadastro[9999]

    lista_usuarios = list(cadastro.values())
    quant = 0
    for i in range(len(lista_usuarios)):
        for j in range(len(lista_usuarios[i])):
            quant += 1
    return quant
   
cadastro = {122: ['andre'], 1234: ['leo','jean'], 9999:['dalton']}
print(quantidade_usuarios(cadastro))

print(cadastro.items())