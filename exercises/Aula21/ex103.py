def ficha(nome="<desconhecido>", gols=0):
    print("nome",nome)
    print("gols",gols)
    return

nome = str(input("Nome:"))
gols = str(input("Gols:"))
if nome.strip() == '':
    if gols.isnumeric():
        ficha(gols=gols)
    else:
        ficha()
else: 
    if gols.isnumeric():
        ficha(nome,gols)
    else:
        ficha(nome)
    
    
