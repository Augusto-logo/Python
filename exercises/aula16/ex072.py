aNumbers = ('zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

number = int(input('Digite um número entre 0 e 20:'))

while True:
    if number >= 0 and number <= 20:
        print(f'Você digitou o número {aNumbers[number]}!')
        break
    else:
        print('Você digitou um número fora do intervalo')
        number = int(input('Digite um número entre 0 e 20:'))
