"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável."""
def escreva(mensagem):
    tamanhoMensagem = len(mensagem) + 4
    print("~"*tamanhoMensagem)
    print(mensagem.center(tamanhoMensagem, " "))
    print("~"*tamanhoMensagem)
    print()

texto = str(input("Digite o texto a ser formatado: "))
escreva(texto)
escreva('um grande texto')