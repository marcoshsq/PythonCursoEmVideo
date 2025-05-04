# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math

num = float(input("Digite um número real: "))
parte_inteira = math.trunc(num)

print("A parte inteira de {} é {}".format(num, parte_inteira))
