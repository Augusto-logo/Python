from random import randint

print('=-' * 20)
print('Vamos jogar PAR ou IMPAR:')
jogada = 'a'
numero = 0
cont = 0
while True:
    print('=-' * 20)
    while numero <= 0:
        numero = int(input('Digite um número:'))
    while jogada not in 'PI':
        jogada = str(input('Escolha entre par e impar [P/I]:')).strip().upper()
    computador = randint(1,10)
    soma = numero + computador
    if soma % 2 == 0:
        if 'I' in jogada:
            print('==' * 20)
            print(f'Você jogou {numero} e o computador {computador}. O total deu {soma} e é PAR!')
            print('==' * 20)
            print('GAME OVER! ')
            print(f'Você venceu {cont} vezes!')
            break
        else:
            print('==' * 20)
            print(f'Você jogou {numero} e o computador {computador}. O total deu {soma} e é PAR!')
            print('Você venceu!')
            print('==' * 20)
            print('Vamos jogar novamente...')
            cont += 1
    else:
        if 'P' in jogada:
            print('==' * 20)
            print(f'Você jogou {numero} e o computador {computador}. O total deu {soma} e é IMPAR!')
            print('==' * 20)
            print('GAME OVER! ')
            print(f'Você venceu {cont} vezes!')
            break
        else:
            print('==' * 20)
            print(f'Você jogou {numero} e o computador {computador}. O total deu {soma} e é IMPAR!')
            print('Você venceu!')
            print('==' * 20)
            print('Vamos jogar novamente...')
            cont += 1
    numero = 0
    jogada = 'a'
