pa = int(input('Digite o primeiro valor da PA:'))
r = int(input('Digite a Razão da PA: '))

for c in range(0,10):
    print(f'{c+1 :2}º termo - {pa + (r * c) :2}')
