import datetime
ano = int(input('Digite o seu ano de nascimento:'))
data = datetime.datetime.now()
data = int(data.strftime('%Y'))

idade = int(data - ano)
if idade > 25:
    print(f'Como sua idade é de {idade} sua categoria é de MASTER!')
elif idade > 19:
    print(f'Como sua idade é de {idade} sua categoria é de SÊNIOR!')
elif idade > 14:
    print(f'Como sua idade é de {idade} sua categoria é de JUNIOR!')
elif idade > 9:
    print(f'Como sua idade é de {idade} sua categoria é de INFANTIL!')
else:
    print(f'Como sua idade é de {idade} sua categoria é de MIRIM!')
