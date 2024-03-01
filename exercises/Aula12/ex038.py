num1 = int(input('Digite um número inteiro:'))
num2 = int(input('Digite outro número inteiro:'))

if num1 > num2:
    print(f'O número {num1} é maior!')
elif num2 > num1:
    print(f'O número {num2} é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')
