from modules.interface import *
def verifyArq(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(txt):
    try:
        a = open(txt, 'wt+')
        a.close()
    except:
        print("Erro ao criar arquivo")
    else:
        print("Arquivo criado")

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo")
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')

