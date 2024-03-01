termo = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite A razão da PA:'))
cont = 10

print('-='*25)
print(termo, end='')
while cont!=1:
    termo += razao
    print(f'-> {termo}', end='')
    cont -= 1
