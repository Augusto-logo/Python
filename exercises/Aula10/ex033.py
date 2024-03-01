num1 = int(input('Digite o primeiro número Inteiro:'))
num2 = int(input('Digite o segundo número Inteiro:'))
num3 = int(input('Digite o terceiro número Inteiro:'))
# 4 2 5
if num1 >= num2 and num1 >= num3:
    print(f'Maior:{num1}')
    if num2 > num3:
        print(f'Menor:{num3}')
    else:
        print(f'Menor:{num2}')
if num2 >= num3 and num2 >= num1:
    print(f'Maior:{num2}')
    if num1 > num3:
        print(f'Menor:{num3}')
    else:
        print(f'Menor:{num1}')
if num3 >= num1 and num3 >= num2:
    print(f'Maior:{num3}')
    if num2 > num1:
        print(f'Menor:{num1}')
    else:
        print(f'Menor:{num2}')

    