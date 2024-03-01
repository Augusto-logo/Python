num = int(input('Digite um número para calcular seu Fatorial:'))
soma = num
cont = 1
lista = []
print(f'Calculando {num}! ', end='')

while num != 1:
    soma = soma * (num - cont)
    lista.append(num)
    num -= 1

for c in range(len(lista), 0, -1):
    print(f'{lista[len(lista) - c]} X ', end='')

print('1 = ', soma)
