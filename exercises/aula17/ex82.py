lista = []
listaPar = []
listaImpar = []
cont = 0
verify = 'S'
while verify.upper() == 'S':
    num = int(input("Digite um número:"))
    lista.append(num)
    cont += 1
    verify = str(input("Deseja Continuar ? [S]:"))
for i in lista:
    if i % 2 == 0:
        listaPar.append(i)
    else:
        listaImpar.append(i)
print(f'Lista completa: {lista}')
print(f'Lista dos pares: {listaPar}')
print(f'Lista dos impares: {listaImpar}')
