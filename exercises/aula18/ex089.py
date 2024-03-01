lista = []
# lista = [["João",4.5,7],["maria", 8, 10],["Pedro", 5, 10]]
temp = []
verify = 'S'

while "S" in verify.upper():
    temp.append(str(input("Digite o nome do aluno:")))
    for i in range (0,2):
        temp.append(float(input(f"Digite a {i+1}º nota:")))
    lista.append(temp[:])
    temp.clear()
    verify = str(input("Deseja Continuar [S]:"))

print('-='*60)
print("BOLETIM ESCOLAR")
print("No. NOME       Media")
print('-'*20)
for i,l in enumerate(lista):
    media = (l[1] + l[2])/2
    print(f'{i}   {l[0]}        {media}')

cont = 0
while cont != -1:
    print('-'*20)
    cont = int(input('Mostrar notas de qual aluno: [-1 interrompe]:'))
    print(f'As notas de {lista[cont][0]} são {lista[cont][1]} e {lista[cont][2]}!')
