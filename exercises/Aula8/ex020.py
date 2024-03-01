import random

var1 = input("Digite o nome do primeiro aluno(a): ")
var2 = input("Digite o nome do segundo aluno(a): ")
var3 = input("Digite o nome do terceiro aluno(a): ")
var4 = input("Digite o nome do quarto aluno(a): ")

alunos = [var1,var2,var3,var4]
random.shuffle(alunos)
print(f'A ordem de alunos escolhidos para apresentar o trabalho foi: \n{alunos[0]} \n{alunos[1]} \n{alunos[2]} \n{alunos[3]}')
