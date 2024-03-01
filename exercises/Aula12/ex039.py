import datetime
ano = int(input('Digite o seu ano de nascimento:'))
data = datetime.datetime.now()
data = int(data.strftime('%Y'))

if data - ano > 18:
    print(f'Já passou do tempo de se alistar em {data - ano - 18} anos!')
elif ano - data == 18:
    print('Está na hora de se alistar!')
else:
    print(f'Você ainda vai se alistar e faltam {ano - data + 18} anos!')
