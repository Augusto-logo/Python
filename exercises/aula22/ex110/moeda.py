def resumo(preço = 0, aumento = 10, redução = 15):
    print('-'*30)
    print('RESUMO DO  VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'O dobro do preço: \t{dobro(preço, True)}')
    print(f'A metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço,aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(preço, redução, True)}')
    print('-'*30)
    return

def aumentar(num = 0, porcentagem = 0, format=False):
    porcentagem = porcentagem/100
    num = num + (num * porcentagem)
    return num if not format else moeda(num)

def diminuir(num = 0, porcentagem = 0, format=False):
    porcentagem = porcentagem/100
    num = num - (num * porcentagem)
    return num if not format else moeda(num)

def dobro(num = 0, format=False):
    resultado = num*2
    return resultado if not format else moeda(resultado)

def metade(num = 0, format=False):
    resultado = num / 2
    return resultado if not format else moeda(resultado)

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:>.2f}'.replace('.',',')

