import random

print('-='*20)
print('Jokenpô')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('-='*20)
player = int(input('Digite sua jogada:'))
computador = random.randint(1,3)

if player == computador:
    if player == 1:
        print('O computador escolheu Pedra e você também, logo é um empate!')
    elif player == 2:
        print('O computador escolheu Papel e você também, logo é um empate!')
    else:
        print('O computador escolheu Tesoura e você também, logo é um empate!')
elif computador == 3 and player == 1:
    print('Você escolheu Pedra e computador escolheu Tesoura, logo você ganhou!')
elif computador == 3 and player == 2:
    print('Você escolheu Papel e computador escolheu Tesoura, logo você Perdeu!')
elif computador == 1 and player == 2:
    print('Você escolheu Papel e computador escolheu Pedra, logo você ganhou!')
elif computador == 1 and player == 3:
    print('Você escolheu Tesoura e computador escolheu Pedra, logo você perdeu!')
elif computador == 2 and player == 1:
    print('Você escolheu Pedra e computador escolheu Papel, logo você perdeu!')
elif computador == 2 and player == 3:
    print('Você escolheu Tesoura e computador escolheu Papel, logo você ganhou!')
else:
    print('Escolha não reconhecida!')
