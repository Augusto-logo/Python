def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número válido')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada interrompida')
            return 0
        else:
            return num

def linha(tam = 42):
    return print('-' * tam)

def cabeçalho(msg):
    linha()
    print(msg.center(42))
    linha()

def menu(lista):
    cabeçalho('MENU')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
    opc = leiaInt('Sua Opção: ')
    return opc