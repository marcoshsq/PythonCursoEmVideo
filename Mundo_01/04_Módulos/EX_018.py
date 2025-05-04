# Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input("Digite o ângulo (em graus): "))

rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print("Para o ângulo de {:.1f}°:".format(angulo))
print("Seno = {:.4f}".format(seno))
print("Cosseno = {:.4f}".format(cosseno))
print("Tangente = {:.4f}".format(tangente))
