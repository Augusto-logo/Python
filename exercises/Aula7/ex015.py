rodado = int(input('Digite quantos KM foi rodado:'))
dias = int(input('Digite por quantos dias ele foi rodado:'))

print(f'Ao rodar por {dias} dias e correr por {rodado} km. \nVocê terá que pagar R${dias * 60} pelos dias percorridos e R${rodado * 0.15} pelos KM rodados. \nTotalizando um valor de R${dias * 60 + rodado * 0.15 :.2f}')
