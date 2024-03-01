nota1 = float(input('Digite a primeira nota do aluno:'))
nota2 = float(input('Digite a segunda nota do aluno:'))

media = (nota1+nota2)/2

if media < 5:
    print(f'Como sua média foi de {media :.2f} você está REPROVADO!')
elif media >= 5 and media < 7:
    print(f'Como sua média foi de {media :.2f} você está em RECUPERAÇÃO!')
else:
    print(f'Como sua média foi de {media :.2f} você está em APROVADO!')
