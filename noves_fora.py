def minha_copia(lista):
    new_list = []
    for e in lista: new_list.append(e)
    return new_list

def meu_insert_ordenado(numero, lista):
    lista.append(numero)
    l = len(lista) - 1
    while l != 0 and lista[l] > lista[l-1]:
        lista[l-1], lista[l] = lista[l], lista[l-1]
        l -= 1

def noves_fora(lista):
    array_etapas= []
    array_etapas.append(minha_copia(lista))

    while len(lista) > 1:
        soma =  lista[0] + lista[1]
        if soma >= 9:
            soma %= 9
        lista.pop(1)
        lista.pop(0)
        meu_insert_ordenado(soma,lista)
        array_etapas.append(minha_copia(lista))
    if lista == [9]:
        lista[0] = 0
        array_etapas.append(minha_copia(lista))

    return lista[0], array_etapas

lista = [9,9]
print(noves_fora(lista))