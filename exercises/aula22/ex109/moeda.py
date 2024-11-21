def aumentar(num = 0, porcentagem = 0, format=False):
    porcentagem = porcentagem/100
    num = num + (num * porcentagem)
    return num if not format else moeda(num)

def diminuir(num = 0, porcentagem = 0, format=False):
    porcentagem = porcentagem/100
    num = num - (num * porcentagem)
    return num if not format else moeda(num)

def dobro(num = 0, format=False):
    return num*2 if not format else moeda(num)

def metade(num = 0, format=False):
    return num/2 if not format else moeda(num)

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:>.2f}'.replace('.',',')

