eq = str(input("Digite a equação:"))
lista = []

for i,v in enumerate(eq):
    if v == '(':
        lista.append(v)
    elif v == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(v)
            break

print(lista)
if len(lista) > 0:
    print('A equação não existe!')
else:
    print('A equação existe!')
