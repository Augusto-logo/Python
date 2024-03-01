print('=' * 30)
print('CADASTRO DE PESSOAS')
print('=' * 30)

totalIdade = TotalHomem = TotalMulher = 0
continuar = 'a'

while True:
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o sexo [M/F]:')).strip().upper()
    if idade >=18:
        totalIdade += 1
    if sexo in 'M':
        TotalHomem += 1
    if sexo in 'F' and idade <20:
        TotalMulher += 1
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]?')).strip().upper()
    if continuar in 'N':
        break
    continuar = 'a'

print(f'Houveram {totalIdade} pessoas com mais de 18 anos')
print(f'Houveram {TotalHomem} Homens cadastrados.')
print(f'Houveram {TotalMulher} Mulheres com menos de 20 anos cadastradas.')
