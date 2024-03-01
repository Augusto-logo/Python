num = int(input('Digite o valor da tabuada:'))

while True:
    cont = 1
    if num < 0:
        break
    print('=='*20)
    while True:
        print(f'{num} X {cont:2} = {num*cont:2}')
        cont += 1
        if cont == 11:
            print('=='*20)
            break
    num = int(input('Digite o valor da tabuada:'))

print('Programa Finalizado')
