def aumentar(num, porcentagem):
    porcentagem = porcentagem/100
    num = num + (num * porcentagem)
    return num

def diminuir(num, porcentagem):
    porcentagem = porcentagem/100
    num = num - (num * porcentagem)
    return num

def dobro(num):
    return num*2

def metade(num):
    return num/2