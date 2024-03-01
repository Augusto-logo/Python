matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPar = 0
maiorLinha = 0
for i in range (0,3):
    for j in range (0,3):
        matriz[i][j] = int(input(f"Digite a posição [{i}][{j}]:"))

maiorLinha = matriz[1][0]

for i in range (0,3):
    for j in range (0,3):       
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            somaPar += matriz[i][j]
        if i == 1 and maiorLinha < matriz[i][j]:
            maiorLinha = matriz[i][j]
    print()
print('-=' * 50)
somaColuna = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores pares digitados foi de: {somaPar}')
print(f'A soma da terceira coluna foi de: {somaColuna}')
print(f'O maior elemento da segunda linha foi o: {maiorLinha}')