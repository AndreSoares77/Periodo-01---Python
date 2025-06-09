palavra = input()
volgais = 'AEIOUaeiou'
new_palavra = ''

for letra in palavra:
    if letra not in volgais: new_palavra += letra

print(new_palavra)