def aumentar(num = 0, porcentagem = 0):
    porcentagem = porcentagem/100
    num = num + (num * porcentagem)
    return num

def diminuir(num = 0, porcentagem = 0):
    porcentagem = porcentagem/100
    num = num - (num * porcentagem)
    return num

def dobro(num = 0):
    return num*2

def metade(num = 0):
    return num/2

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:>.2f}'.replace('.',',')

