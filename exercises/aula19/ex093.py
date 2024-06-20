jogador = dict()
listaGols = list()
numGols = int(0)
jogador["nome"] = str(input("Digite o nome do jogador: "))
numPartidas = int(input("Digite o número de partidas jogadas: "))

for i in range(1,numPartidas + 1):
    gol = int(input(f"Quantidade de gols do jogo {i}:"))
    listaGols.append(gol)
    numGols = numGols + gol

jogador["gols"] = listaGols[:]
jogador["total"] = numGols
print("-=" * 30)
print(jogador)
print("-=" * 30)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}!")
    
print("-=" * 30)
print(f"O jogador {jogador['nome']} jogou {numPartidas} partidas!")
for i in range(0,numPartidas):
    print(f"     => Na partida {i+1}, fez {jogador["gols"][i]} gols!")
print(f"O jogador {jogador['nome']} fez um total de {jogador['total']} gols!")
print("-=" * 30)
    
