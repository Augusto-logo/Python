array = ('ana', 'carro', 'mulher', "Jorge",'Clara','Madeira')

for i in range(0, len(array)):
    print(f'\n{array[i]} tem ', end='')
    if 'a' in array[i]:
        print('a ', end='')
    if 'e' in array[i]:
        print('e ', end='')
    if 'i' in array[i]:
        print('i ', end='')
    if 'o' in array[i]:
        print('o ', end='')
    if 'u' in array[i]:
        print('u ', end='')
