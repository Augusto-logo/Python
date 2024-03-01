distancia = int(input('Digite a distância em KM da sua viagem:'))
if distancia <= 200:
    print(f'Numa distância de {distancia}KM, sua passagem custará R${distancia * 0.50}!')
else:
    print(f'Numa distância de {distancia}KM, sua passagem custará R${distancia * 0.45}')
