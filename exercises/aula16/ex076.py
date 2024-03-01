array = ('Lápis',1.75,'Borracha',2.00,'Estojo',25.00,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)

str = 'LISTAGEM DE PREÇOS'

print("--"*20)
print(str.center(40))
print("--"*20)

for i in range(0, len(array)):
    if i % 2 == 0:
        print(f'{array[i]:.<30}', end='')
    else:
        print(f'R${array[i]:>7.2f}')
