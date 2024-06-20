from datetime import datetime
pessoa = {}
pessoa["nome"] = input("Nome: ")
dataNasc = int(input("Ano de nascimento: "))
carteiraDeTrabalho = int(input("Carteira de trabalho (0 se não tiver): "))
date = datetime.now().year
pessoa["idade"] = date - dataNasc

if carteiraDeTrabalho > 0:
    pessoa["anoContratação"] = int(input("Digite o ano da sua contratação: "))
    pessoa["salario"] = float(input("Digite o seu salário: "))
    pessoa["idadeAposentar"] = pessoa["idade"] + (pessoa["anoContratação"] + 35 - date)

print("-=" * 30)
print(pessoa)



