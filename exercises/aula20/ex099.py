def maior(*param):
    if not len(param):
        return print("Lista vázia")
    i = 0
    maior = param[i]
    for i in range(len(param)):
        if (param[i] > maior):
            maior = param[i]
    print(f"O maior valor foi o {maior} de {len(param)} valores!")
    return

maior(1, 52, 37, 48, 80, 92, -105, 0, 102, 38, 42)