def fatorial(num, show=False):
    """
    -> Calcuila o fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) mostrar ou não o calculo.
    :return: O valor do Fatorial de um número num.
    """
    f = 1
    for i in range (num, 0, -1):
        if (show):
            print(i, end='')
            if i>1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f

print(fatorial(5))
print(fatorial(10, True))