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

def leiaFloot(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número válido')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada interrompida')
            return 0
        else:
            return num

numero = leiaInt('Digite um número inteiro: ')
print(numero)
numeroFloot = leiaFloot('Digite um floot: ')
print(numeroFloot)