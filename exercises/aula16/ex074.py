from random import randint

arrayNum = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))

print(f"O computador gerou 5 números aleatórios, eles são: \n {arrayNum}")
print(f'O maior valor gerado foi {max(arrayNum)} e o menor foi {min(arrayNum)}!')
