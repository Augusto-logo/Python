num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
choice = 1

while choice != 5:
    print('='*40)
    print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
    ''')
    choice = int(input('Escolha uma das opções acima:'))
    print('='*40)

    if choice == 1:
        print(f'A soma: {num1} + {num2} = {num1 + num2}!')
    elif choice == 2:
        print(f'A multiplicação: {num1} X {num2} = {num1 * num2}!')
    elif choice == 3:
        if num1 > num2:
            print(f'{num1} > {num2}!')
        elif num2 > num1:
            print(f'{num2} > {num1}!')
        else:
            print(f'{num1} = {num2}!')
    elif choice == 4:
        num1 = float(input('Digite um novo primeiro número:'))
        num2 = float(input('Digite um novo segundo número:'))
    elif choice == 5:
        print('Programa Finalizado!')
    else:
        print('Opção Inválida, Digite novamente!')
