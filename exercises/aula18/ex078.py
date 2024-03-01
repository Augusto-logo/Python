lista = []

for c in range(0,5):
    lista.append(int(input("Digite um número:")))
maior = int(lista[0])
menor = int(lista[0])
for i in range(0,len(lista)):
    if lista[i] < menor:
        menor = lista[i]
    elif lista[i] > maior:
        maior = lista[i]

print(f'O maior valor foi o {maior} na(s) posição(ões) ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'...{i}', end='')
print(f'\nO menor foi {menor} na(s) posição(ões) ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'...{i}', end='')