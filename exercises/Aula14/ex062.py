termo = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite A razão da PA:'))
cont = 10

print('-='*25)
print(termo, end='')
while cont!=0:
    termo += razao
    print(f'-> {termo}', end='')
    if cont == 1:
        print('\n')
        print('=-'*30)
        cont = int(input('\nQuantos termos você quer mostrar a mais ?'))
    else:
        cont -= 1
print('FIM')
