frase = str(input('Digite uma frase:')).strip().lower()
frase = frase.replace(' ','')
fraseInversa = []

for c in range(1, len(frase) + 1):
    fraseInversa.append(frase[len(frase) - c])
    # print(fraseInversa[c])
fraseNova = ''.join(fraseInversa)

if fraseNova == frase:
    print('É palíndromo')
else:
    print('Não é um Palíndromo')
