from random import randint
import time
from operator import itemgetter
jogadoresDict = {}
ranking = dict()

for i in range (1,5):
    jogador = 'jogador' + str(i)
    dado = randint(1,6)
    jogadoresDict[jogador] = dado
    time.sleep(1)
    print(f'O {jogador} tirou {dado}!')
print("-="*30)
print("----RANKING----")
ranking = sorted(jogadoresDict.items(), key=itemgetter(1), reverse=True)
for k,v in enumerate(ranking):
    print(f"O {k+1}º lugar: {v[0]} com {v[1]}.") 

