frase = input('Digite uma frase:').strip().upper()
print(f'No seu texto a letra A apareceu {frase.count("A")}')
print(f'A primeira letra A apareceu na posição {frase.rfind("A") +1}')