def reorganiza_lista(l):
    pos_termo_central = 0

    if len(l) % 2 != 0:
        pos_termo_central = len(l)//2 + 1
        termo_central = l.pop(pos_termo_central)

    parte01 = []
    parte02 = []

    for i in range(len(l)//2):
        parte01.append(l[i])
    for e in range(len(l)-1,len(l)//2 - 1, -1):
        parte02.append(l[e])
        

    j = len(l)
    l = []
    p1 = 0
    p2 = 0

    for h in range(j):
        if h % 2 == 0:
            l.append(parte01[p1])
            p1 += 1
        else:
            l.append(parte02[p2])
            p2 += 1
        if p2 == len(parte02):break

    if pos_termo_central != 0:
        l.append(termo_central)
        while j != pos_termo_central:
            l[j-1],l[j] = l[j],l[j-1]
            j -= 1

    return l


l1 = [1,2,3,4,5]
l2 = [1,2,3,4]
print(reorganiza_lista(l1))
print(reorganiza_lista(l2))