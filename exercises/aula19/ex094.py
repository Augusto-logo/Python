""" Enunciado
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
# Inicialização das variáveis do CRUD
listaPessoas = list()
dictPessoa = dict()
continuar = ''
cont = 1
sexo = ''
# CRUD
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
# Variáveis dos dados das perguntas
totalPessoas = len(listaPessoas)
totalIdade = 0
mediaIdade = 0
listaMulheres = list()
listaAcimaMedia = list()
# Manipulação dos dados das listas e dos dicionários
for i in range(0,len(listaPessoas)):
    totalIdade = totalIdade + listaPessoas[i]["idade"]
mediaIdade = totalIdade/totalPessoas

for i in range(0, len(listaPessoas)):
    if listaPessoas[i]["sexo"] == "F":
        listaMulheres.append(listaPessoas[i])

for i in range(0,len(listaPessoas)):
    if listaPessoas[i]["idade"] > mediaIdade:
        listaAcimaMedia.append(listaPessoas[i])

# Prompt das perguntas 
print("-="*25)
print(f"A)O número total de pessoas cadastradas foi de: {totalPessoas}")
print(f"B)A média de idade de pessoas cadastradass foi de: {mediaIdade}")
print(f"B)A lista de mulheres é: {listaMulheres}")
print(f"D)As pessoas com a idade acima da media  foram: {listaAcimaMedia}")
print("-="*25)
