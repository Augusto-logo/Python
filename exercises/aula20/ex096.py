"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""
def área(largura, comprimento):
    return print(f"A área tem {largura * comprimento}M².")


largura = int(input("Lagura: "))
comprimento = int(input("Comprimento: "))
área(largura,comprimento) 