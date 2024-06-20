listaPessoas = list()
dictPessoa = dict()
continuar = ''
cont = 1
sexo = ''
while True:
    dictPessoa.clear()
    dictPessoa["nome"] = str(input("NOME: "))
    while True:
        dictPessoa["sexo"] = str(input("SEXO: [M/F]: ")).upper()[0]
        if dictPessoa["sexo"] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    dictPessoa["idade"] = int(input(f"IDADE: "))
    listaPessoas.append(dictPessoa.copy())
    while True:
        continuar = str(input("Deseja continuar ? [S/N]: ")).upper()[0]
        if continuar in "SN":
            break
        print("ERRO! Digite apenas S ou N;")
    if continuar == 'N':
        break
print(listaPessoas)
print("-="*25)
print(f"A)O número total de pessoas cadastradas foi de: {len(listaPessoas)}")
print("-="*25)
