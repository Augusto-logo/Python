""" Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
from time import sleep
def contador(inicio, fim, passo):
    if passo <= 0:
        if passo == 0:
            passo = 1
        else:
            passo = abs(passo)
    if inicio < fim:
        valor = inicio
        while True:
            if valor >= fim:
                print(fim, end=" ")
                print("FIM!")
                break
            print(valor, end=" ", flush= True)
            sleep(0.5)
            valor += passo
    elif fim < inicio:
        valor = inicio
        while True:
            if valor <= fim:
                print(fim, end=" ")
                print(" FIM!")
                break
            print(valor, end=" ", flush= True)
            sleep(0.5)
            valor -= passo
        

contador(1,10,1)
contador(10,0,2)
contador(10,100,-8)