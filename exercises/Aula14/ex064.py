num = 0
soma = -999
cont = -1

while num != 999:
    num = int(input('Digite um número[999 stop program]: '))
    soma += num
    cont += 1

print('=-'*40)
print(f'Foram digitados {cont} números e a soma foi deles foi de {soma}!')
