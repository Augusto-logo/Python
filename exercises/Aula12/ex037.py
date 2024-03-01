num = int(input('Digite um número inteiro:'))

print('-='*20)
print('1 - binário.')
print('2 - octal.')
print('3 - hexadecimal.')
print('-='*20)

decisao = int(input('Escolha um dos métodos de conversão:'))

if decisao == 1:
    print(f'O número {num} em binário é {bin(num)[2:]}')
elif decisao == 2:
    print(f'O número {num} em octal é {oct(num)[2:]}')
elif decisao == 3:
    print(f'O número {num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Nenhuma escolha reconhecida!')
