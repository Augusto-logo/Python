lado1 = int(input('Digite o tamanho da primeira reta:'))
lado2 = int(input('Digite o tamanho da segunda reta:'))
lado3 = int(input('Digite o tamanho da terceira reta:'))

if lado1 < lado2+lado3 and lado2 <lado1+lado3 and lado3 < lado1+lado2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')