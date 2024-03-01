sex = str(input('Digite um sexo: [M/F]')).strip().upper()
while sex not in('M','F'):
    sex = str(input('Input não reconhecido. Por favor, digite seu sexo:')).strip().upper()

print(f'Sexo {sex} Digitado com sucesso!')