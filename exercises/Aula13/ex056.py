somaIdade = 0
maiorIdade = 0
nomeMaiorIdade = ""
totalIdadeMulher = 0
for c in range(1,5):
    print('======== {c}ª PESSOA ========')
    nome = input('Nome:').strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().upper()
    if c == 1 and sexo == 'M':
        maiorIdade = idade
        nomeMaiorIdade = nome
    if sexo == 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomeMaiorIdade = nome
    somaIdade += idade
    if sexo == 'F' and idade < 20:
        totalIdadeMulher += idade
print(f'A média de idade do grupo é de {somaIdade / 4 :.2f}!')
print(f'O homem mais velho tem {maiorIdade} anos e se chama {nomeMaiorIdade}!')
print(f'Há um total de {totalIdadeMulher} mulheres com menos de 20 anos!')
