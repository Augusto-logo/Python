num = int(input('Digite um número: '))
i = 0
if num < 0:
    print(f'O número {num} é negativo, portanto não é primo!')
elif num == 1:
    print(f'O número {num} não é primo!')
elif num == 2:
    print(f'O número {num} é primo!')
else:
    for c in range(1, int(num / 2) + 1):
        if num % c == 0:
            i += 1
    if i == 1:
        print(f'O número {num} é primo!')
    else:
        print(f'O número {num} não é primo!')
