l1 = [2,3]
l2 = [1,2,3]

new_l1 = ''
for i in range(len(l1)-1,-1,-1):
    new_l1 += (str(l1[i]))

new_l2 = ''
for j in range(len(l2)-1,-1,-1):
    new_l2 += (str(l2[j]))

new_l1 = int(new_l1)
new_l2 = int(new_l2)

soma = new_l2 + new_l1
soma = str(soma)

list_soma = []

for k in range(len(soma)):
    list_soma.append(int(soma[k]))

print(list_soma)