def reorganiza_l2(lenl2,l2):
    destino = 0
    for x in range(lenl2, len(l2)):
        n = x
        while True:
            if n == destino: break
            l2[n-1],l2[n] = l2[n],l2[n-1]
            n -=1
        destino += 1
                       
def reorganiza(l1,l2):
    for i in range(len(l2)):
        if l2[i] % 2 != 0:
            l1.append(l2[i])

    for l in range(len(l2)-1,-1,-1):
        if l2[l] % 2 != 0:
            l2.pop(l)

    lenl2 = len(l2)

    for j in range(len(l1)):
        if l1[j] % 2 == 0:
            l2.append(l1[j])
    
    for h in range(len(l1)-1,-1,-1):
         if l1[h] % 2 == 0:
            l1.pop(h)
    
    reorganiza_l2(lenl2, l2)

    return l1,l2



l1 = [5,20,10,7,9,8]
l2 = [8,3,2,1,30]

print(reorganiza(l1,l2))



