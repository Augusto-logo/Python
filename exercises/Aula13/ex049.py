from time import sleep
num = int(input('Digite um número:'))

print('-='*10)
for c in range(1,11):
    print(f'{num} X {c :2} = {num * c}')
    sleep(0.3)
print('-='*10)