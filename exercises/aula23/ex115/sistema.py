from modules.interface import *
from modules.archives import *
from time import sleep

arq = 'pessoa.txt'

if not verifyArq(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #Listar conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('SAIDO DO SISTEMA')
        break
    else:
        print('Comando não reconhecido')
    sleep(2)