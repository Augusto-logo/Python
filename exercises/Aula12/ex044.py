preço = float(input('Digite o preço do Produto:'))

a = '\033[1;33;57m'
b = '\033[m'

print('-='*20)
print('Métodos de pagamento:')
print(f'1 - À vista em {a}dinheiro{b}, 10% de desconto!')
print('2 - À vista no cartão  , 5% de desconto!')
print('3 - Em até 2x no cartão, preço see juros!')
print('4 - 3x ou mais no cartão, 20% de juros!')
print('-='*20)
metodo = int(input('Digite o método de pagamento:'))

if metodo == 1:
    print(f'O valora ser pago com dinheiro é de: R${preço*0.90 :.2f}')
elif metodo == 2:
    print(f'O valora ser pago à vista no cartão é de: R${preço*0.95 :.2f}')
elif metodo == 3:
    print(f'O valora ser pago em até 2x no cartão é de: R${preço:.2f}')
    print(f'Sendo R${preço/2 :.2f} o valor de cada parcela.')
elif metodo == 4:
    parcela = int(input('Digite quantas parcelas:'))
    print(f'O valora a ser pago em {parcela}x no cartão é de: R${preço*1.20:.2f}')
    print(f'Sendo R${(preço*1.20)/parcela :.2f} o valor de cada parcela.')
else:
    print('Método de pagamento inválido!')
