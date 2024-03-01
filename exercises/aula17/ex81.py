lista = []
cont = 0
verify = 'S'
while verify.upper() == 'S':
    num = int(input("Digite um número:"))
    lista.append(num)
    cont += 1
    verify = str(input("Deseja Continuar ? [S]:"))
print(f"Foram digitados {cont} números")
lista.sort(reverse=True)
print(f"A lista em ordem decrescente é {lista}")
if 5 in lista:
    print("O valor 5 foi digitado!")
else:
    print("O valor 5 não foi digitado!")
