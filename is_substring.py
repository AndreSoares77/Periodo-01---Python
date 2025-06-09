def is_substring(str1, str2):
    for i in range(len(str1)-len(str2)+1):
        if str1[i] == str2[0]:
            cont = 1
            l = i + 1
            for h in range(1, len(str2)):
                if str2[h] == str1[l]:
                    cont += 1
                l += 1
            if cont == len(str2):
                return True
    return False


str1 = 'ioooooooooooooooi'
str2 = 'oi'

print(is_substring(str1, str2))
