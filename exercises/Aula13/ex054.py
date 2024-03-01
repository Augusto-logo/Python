from datetime import date
pessoas = []
dataNow = date.today().year
for c in range(0,7):
    data = int(input('Digite sua data de Nascimento:'))
    if dataNow - data >= 18:
        pessoas.append('ATINGIU A MAIORIDADE')
    else:
        pessoas.append('NÃO ATINGIU A MAIORIDADE')
for k in range(0,7):
    print(f'A {k+1}º pessoa {pessoas[k]}!')
