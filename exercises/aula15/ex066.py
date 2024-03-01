num = cont = 0
soma = 0
while True:
    num = int(input('Digite um numero[stop = 999]:'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} números e a soma deles foi de {soma}')
