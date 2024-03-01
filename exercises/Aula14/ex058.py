import random
print('O computador pensou num número de 0 a 5.')
numComputador = random.randint(0,10)
num = int(input('Tente adivinhar o número:'))
cont = 1
while numComputador != num:
    num = int(input('Número errado.Tente adivinhar de novo:'))
    cont += 1
print(f'Parabéns, você acertou em {cont} tentativas!')
