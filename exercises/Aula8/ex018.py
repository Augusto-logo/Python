import math

angulo = float(input('Digite um ângulo: '))
angulo_rad = math.radians(angulo)
print(f'Baseado no angulo {angulo}º o seu cosseno é: {math.cos(angulo_rad) :.2f} e seu seno é: {math.sin(angulo_rad) :.2f}')