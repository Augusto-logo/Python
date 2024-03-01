casa = float(input('Digite o valor da casa:'))
salario = float(input('Digite o seu salário:'))
anos = int(input('Digite em quantos anos irá pagar:'))

prestação = casa / (anos * 12)

if prestação <= salario * 0.30:
    print(f'A prestação mensal custará R${prestação :.2f}, portanto, Crédito aprovado!')
else:
    print(f'A prestação mensal custará R${prestação :.2f}, portanto, Crédito negado!')
