# nome media e mostrar situação
nome = str(input("Digite o nome do aluno:"))
situação = ''
dicionario = {}
i = 1

while i != 0:
    media = float(input(f"Digite a média do aluno {nome}:"))
    if media >= 7:
        situação = "Aprovado!"
        i = 0
    elif media >= 5:
        situação = "Recuperação!"
        i = 0
    elif media >= 0:
        situação = "Reprovado!"
        i = 0
    else: 
        print("Nota invalida, tente novamente!")
        i = 1
dicionario = {"Nome": nome, "Nota": media, "Situação": situação}
print("-=" * 30)
for k,v in dicionario.items():
    print(f"O(a) {k} do aluno(a) é {v}")
