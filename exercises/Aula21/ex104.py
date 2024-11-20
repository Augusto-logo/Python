def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

n = leiaInt('Digite um número: ')
print(f'Você digitou {n}')