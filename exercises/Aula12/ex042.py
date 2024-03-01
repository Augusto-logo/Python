lado1 = int(input('Digite o tamanho da primeira reta:'))
lado2 = int(input('Digite o tamanho da segunda reta:'))
lado3 = int(input('Digite o tamanho da terceira reta:'))

if lado1 < lado2+lado3 and lado2 <lado1+lado3 and lado3 < lado1+lado2:
    if lado1 == lado2 and lado2 == lado3:
        print('É possível formar um triângulo e ele é Equilátero!')
    elif lado1 == lado2 and lado2 != lado3:
        print('É possível formar um triângulo e ele é Isósceles!')
    else:
        print('É possível formar um triângulo e ele é Escaleno!')
else:
    print('Não é possível formar um triângulo!')
