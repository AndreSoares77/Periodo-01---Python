matriz = [[1, 1, 1, 1, 1, 1],
          [1, 2, 2, 2, 2, 1],
          [1, 2, 3, 3, 2, 1],
          [1, 2, 3, 3, 2, 1],
          [1, 2, 2, 2, 2, 1],
          [1, 1, 1, 1, 1, 1]]

# i = linhas
# j = colunas

k = 5

#k = moldura q quero somar

soma = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == k and j >= k and j <= (len(matriz[i]) - 1 - k):                              #linha k
            soma += matriz[i][j]

        elif i == ((len(matriz)) - 1 - k) and j >= k and j <= (len(matriz[i]) - 1 - k):      #linha (len(matriz)-1-k)
            soma += matriz[i][j]

        elif i > k and i < (len(matriz) -1 -k) and (j == k or j == (len(matriz[i]) -1 -k)):  #elementos do meio
            soma += matriz[i][j]

print(soma)