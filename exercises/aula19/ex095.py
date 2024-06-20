# Enunciado
# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# Váriaveis do CRUD
jogadores = list()
jogador = dict()
listaGols = list()
numGols = int(0)
continuar = ''
# CRUD
while True:
    jogador.clear()
    listaGols.clear()
    jogador["nome"] = str(input("Digite o nome do jogador: "))
    numPartidas = int(input("Digite o número de partidas jogadas: "))
    for i in range(1,numPartidas + 1):
        gol = int(input(f"Quantidade de gols do jogo {i}:"))
        listaGols.append(gol)
        numGols = numGols + gol
    jogador["gols"] = listaGols[:]
    jogador["total"] = numGols
    jogadores.append(jogador.copy())
    while True:
        continuar = str(input("Deseja continuar[S/N]: "))[0].upper()
        if continuar in 'SN':
            break
        print("Digite apenas S ou N")
    if continuar in 'N':
        break
# Prompt dos resultados + manipulações finais do CRUD
print('-= * 30')
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print("-"*40)
for k,v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
# Visualização individual dos jogadores
while True:
    busca = int(input('Mostrar dados de qual jogador ?(999 PARA)'))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print('Jogador não encontrado!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        for i,g in enumerate(jogadores[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols!')
    print('-' * 40)

