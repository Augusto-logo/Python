lista = []
c = ''
while c != "n".lower():
    num = int(input("Digite um número:"))
    if num in lista:
        print(f"O número {num} não pode ser adicionado pois já há uma cópia dele.")
    else:
        lista.append(num)
    c = str(input("Deseja continuar ?[S/N] "))
lista.sort()
print(f'A lista em ordem crescente foi: {lista}')
