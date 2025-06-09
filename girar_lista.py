def giralista(l1,k):
    j = len(l1) -1
    for i in range(k):
        while j != 0:
            l1[j-1],l1[j] = l1[j],l1[j-1]
            j-=1
        j = len(l1) -1
    return l1


l1 = [1,2,3,4,5]
k = 1
print(giralista(l1,k))