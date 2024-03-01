import math

catOposto = float(input('Digite o cateto oposto:'))
catAdjascente = float(input('Digite o cateto adjascente:'))

print(f'A hipotenusa gerada pelos catetos {catOposto} e {catAdjascente} é igual a {math.hypot(catOposto, catAdjascente)}')