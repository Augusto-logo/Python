lista = []
for i in range(0,5):
    num = int(input("Digite um valor:")) #9
    if not lista: 
        lista.append(num)
        print(f'O número {num} foi adicionado na posição de número 0.')
    elif num <= lista[0]:
        lista.insert(0,num)
        print(f'O número {num} foi adicionado na posição de número 0.')
    elif num >= lista[-1]:
        lista.append(num)
        print(f'O número {num} foi adicionado na posição de número {len(lista)}.')
    else:
        cont = 0
        while cont < len(lista):
            if num <= lista[cont]:
                lista.insert(cont, num)
                break
            cont += 1
print(f'A lista digitada foi:{lista}')
