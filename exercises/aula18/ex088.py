from random import randint
from time import sleep
lista = [[]]
temp = []
num = 0
total = 1
jogos = int(input("Digite Quantos jogos a serem sorteados:"))
while total <= jogos:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    lista.append(temp[:])
    temp.clear()
    total += 1

print('-='*60)
for i in range (1,jogos+1):
    print(f'O {i}º jogo é {lista[i]}')
    sleep(1)
