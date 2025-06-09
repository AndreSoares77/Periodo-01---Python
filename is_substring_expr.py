def is_substring_expr(str1, str2):

    str2 = str2.split('*')

    assert len(str1) >= len(str2[0]) and len(str1) >= len(str2[1])  # contrato*

    palavra1 = str2[0]
    palavra2 = str2[1]
    cont1 = 0
    cont2 = 0

    for i in range(len(palavra1)):
        if palavra1[i] == str1[i]:
            cont1 += 1

    h = -1
    for l in range(len(palavra2)-1, -1, -1):
        if palavra2[l] == str1[h]:
            cont2 += 1
        h -= 1

    return cont1 == len(palavra1) and cont2 == len(palavra2)


str1 = 'oooigggggggggggggggggggggggggggggggggvoce'
str2 = 'oooi*voce'

print(is_substring_expr(str1, str2))
