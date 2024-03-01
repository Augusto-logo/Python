import random

var1 = input("Digite o nome do primeiro aluno(a): ")
var2 = input("Digite o nome do segundo aluno(a): ")
var3 = input("Digite o nome do terceiro aluno(a): ")
var4 = input("Digite o nome do quarto aluno(a): ")

aluno = [var1,var2,var3,var4]

escolhido = random.choice(aluno)

print(f'O aluno(a) escolhido para apagar o quadro foi: {escolhido}')
