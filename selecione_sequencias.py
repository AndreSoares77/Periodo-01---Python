valor_alvo = int(input())

entrada = 0
seq = ''

while True:
    sequencia = input()

    if sequencia == 'fim':
        break
    
    entrada += 1
    cont = 0
    
    for i in range(len(sequencia.split())):

        if valor_alvo < int(sequencia.split()[i]):
            cont += 1
    
    if cont > (len(sequencia.split()) / 2):
        seq += 'Sequência ' + str(entrada) + ': ' + sequencia + ','

lista_sequencia = seq.split(',')
for e in range(len(lista_sequencia)):
    print(lista_sequencia[e])