m= [[1, 2, 3, 4, 5],
    [14,15,16,17,6],
    [13,20,19,18,7],
    [12,11,10,9, 8]]

lista = []
#quant_elem = len(m) * len(m[0])
lim_cima = 0
lim_baixo = len(m)
lim_dir = len(m[0])
lim_esq = 0

while True:
    if len(lista) >= len(m) * len(m[0]):break
    #linha de cima
    for j in range(lim_esq, lim_dir):
        lista.append(m[lim_cima][j])
    lim_cima += 1
    if len(lista) >= len(m) * len(m[0]):break
    #linha da direita
    for i in range(lim_cima, lim_baixo):
        lista.append(m[i][lim_dir - 1])
    lim_dir -= 1
    if len(lista) >= len(m) * len(m[0]):break
    #linha de baixo
    if lim_cima <= lim_baixo:
        for j in range(lim_dir -1, lim_esq -1, -1):
            lista.append(m[lim_baixo-1][j])
        lim_baixo -= 1
    #linha da esquerda
    if lim_esq <= lim_dir:
        for i in range(lim_baixo -1, lim_cima -1, -1):
            lista.append(m[i][lim_esq])
        lim_esq += 1

print(lista)
    
resultado = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2]