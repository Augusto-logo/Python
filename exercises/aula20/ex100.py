from random import randint


def sorteio(lista):
    """
    -> Sorteia 5 números e adiciona numa lista
    :param lista: Lista vazia
    :return: Retorna um print da lista com valores aleatórios.
    """
    for i in range(5):
        lista.append(randint(0,100))
    return print(lista)

def somaPar(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]
    return print(f"A soma dos valores foi de: {soma}")

num = list()
# sorteio(num)
# somaPar(num)
help(sorteio)