num1 = int(input('Digite um número:'))
num2 = int(input('Digite um número:'))
num3 = int(input('Digite um número:'))
num4 = int(input('Digite um número:'))
cont = 0

arrayNumber = (num1,num2,num3,num4)

if 9 in arrayNumber:
    print(f'(A) O número 9 apareceu {arrayNumber.count(9)} vezes!')
else:
    print("(A) O valor 9 não foi digitado nenhuma vez!")

if 3 in arrayNumber:
    print(f'(B) A primeira posição que aparece o valor "3" é na posição: {arrayNumber.index(3)+1}!')
else:
    print('(B) O valor 3 não foi digitado nenhuma vez!')


for i in range(1,len(arrayNumber)):
    if arrayNumber[i-1] % 2 == 0:
        if cont == 0:
            print("Os valores pares foram:")
            cont += 1
        print(arrayNumber[i-1])

if cont == 0:
    print("Não houveram valores pares!")
