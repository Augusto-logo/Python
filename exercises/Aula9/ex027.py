nome = input('Digite seu nome completo:').strip()
listanome = nome.split()
print(f'Primeiro Nome = {listanome[0]}')
print(f'Ultimo nome   = {listanome[len(listanome ) - 1]}')