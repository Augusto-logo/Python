cidade = input('Digite o nome da sua cidade:').strip().upper()
listacidade = cidade.split()
res = listacidade[0].find('SANTO')
print(f'É verdade que a cidade {cidade} começa com a palavra SANTO? se res = 0 sim, =-1 não  res({res}) ')