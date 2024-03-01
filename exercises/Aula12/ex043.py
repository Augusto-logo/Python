peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura em Metros:'))

imc = peso/(altura ** 2)
print(f'Seu IMC é de {imc :.2f}')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >=18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >=25 and imc <30:
    print('Você está no Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está em Obesidade.')
else:
    print('Você está em Obesidade Mórbida.')
