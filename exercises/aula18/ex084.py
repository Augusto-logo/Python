pessoas = []
dadosPessoa = []
verify = 'S'
pesada = 0
leve = 0
while verify.upper() == 'S':
    nome = str(input("Digite o nome da pessoa:"))
    peso = float(input("Digite o peso da pessoa:"))
    dadosPessoa.append(nome)
    dadosPessoa.append(peso)
    if len(pessoas) == 0:
        pesada = leve = peso
    else:
        if peso > pesada:
            pesada = peso
        if peso < leve:
            leve = peso
    pessoas.append(dadosPessoa[:])
    dadosPessoa.clear()
    verify = str(input('Deseja adicionar outra pessoa ? [S]:'))

print(f'O total de pessoas foi: {len(pessoas)}')
print(f'O maior peso foi de {pesada} KG. ', end='')
for i in pessoas:
    if i[1] == pesada:
        print(f'De {i[0]}. ', end='')
print(f'\nO menor peso foi de {leve} KG.')
for i in pessoas:
    if i[1] == leve:
        print(f'De {i[0]}. ', end='')

