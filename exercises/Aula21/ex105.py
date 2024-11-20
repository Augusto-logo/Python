def notas(*notas, situação=False):
    """Recebe uma lista de notas e retorna um dicionário com o total de notas, a maior e menor nota, a média e a situação(Opcional).

    Returns:
        dict: Informações sobre as notas
    """
    Total = len(notas)
    
    maior = menor = notas[0]
    for i in range(1,Total):
        if notas[i] > maior:
            maior = notas[i]
        if notas[i] < menor:
            menor = notas[i]
    
    media = sum(notas)/len(notas)

    resultados = {
        "Total": Total,
        "Maior nota": maior,
        "Menor nota": menor,
        "Media": media,
    }
    if situação:
        if media <= 5:
            situação = "RUIM"
        if media > 5 and media < 7:
            situação = "RAZOÁVEL"
        if media >=7:
            situação = "BOA"
        resultados["Situação"] = situação
    return resultados

resultados = notas(9.1,5.2,8.3,6, situação=True)
print(resultados)