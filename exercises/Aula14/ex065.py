num = soma = cont = menor = 0


print('--== Digite Números ==--')
num = float(input('Digite um numero:'))
verifica = str(input('Deseja continuar ? [S/N]')).lower().strip()[0]

maior = float(num)
menor = float(num)
while verifica in 's':
    num = float(input('Digite um numero:'))
    verifica = str(input('Deseja continuar ? [S/N]'))
    soma += float(num)
    cont += 1
    if float(num) > maior:
        maior = float(num)
    elif float(num) < menor:
        menor = float(num)

print(f'A média dos valores? {soma/cont}')
print(f'O maior valor foi o: {maior}')
print(f'O menor valor foi o: {menor}')
