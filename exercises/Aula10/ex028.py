import random
print('O computador pensou num número de 0 a 5.')
numComputador = random.randint(0,5)
num = int(input('Tente adivinhar o número:'))
print(f'O computador escolheu o numero {numComputador} e você escolheu o numero {num}')
if(num == numComputador):
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você errou')

