velocidade = int(input('Digite a velocidade do carro:'))
if velocidade > 80:
    print(f'O carro ultrapassou a velocidade em {velocidade-80}KM/H')
    print(f'Logo, ele terá que pagar uma multa de R${(velocidade-80)*7}')
