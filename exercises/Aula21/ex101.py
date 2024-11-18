from datetime import datetime

def voto(data):
    if not data:
        return print("Data não informada!")
    dataAtual = datetime.now().year
    data = int(data)
    idade = dataAtual - data
    if (idade >= 65 or idade <18 and idade > 15):
        return print("Voto Opcional",idade)
    if (idade >= 18 and idade < 65):
        return print("Voto Obrigatório", idade)
    return print("Voto Negado", idade)

data = ""
data1 = "2002"
data2 = "2007"
data3 = "1922"
data4 = "2017"
voto(data)
voto(data1)
voto(data2)
voto(data3)
voto(data4)
    