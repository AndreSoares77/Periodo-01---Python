def rotaciona_90(m):
    new_matriz = []
    for j in range(len(m[0])):
        new_linha = []
        for i in range(len(m)-1,-1,-1):
            new_linha.append(m[i][j])
        new_matriz.append(new_linha)

    return new_matriz

m = [[1, 2, 3, 'x'],
     [1, 2, 'x', 4],
     [1, 'x', 3, 4],
     ['x', 2, 3, 4]]

print(rotaciona_90(m))