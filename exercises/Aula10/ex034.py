salario = float(input('Digite o salário do funcionário!'))

if salario > 1250.00:
    print(f'O novo salário é de: R${salario*1.10}')
else:
    print(f'O novo salário foi é de:{salario*1.15}')
