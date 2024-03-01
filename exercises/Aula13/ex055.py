menor = 0
maior = 0
menor = float(input('Digite o peso:'))
maior = menor
for c in range(0,4):
    peso = float(input('Digite o peso:'))
    if menor > peso:
        menor = peso
    elif peso > maior:
        maior = peso
print(f'O menor peso foi de :{menor} KG')
print(f'O maior peso foi de :{maior} KG')
