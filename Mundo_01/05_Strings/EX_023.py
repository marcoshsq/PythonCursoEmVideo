# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

# ex.: digite um número: 1834
# unidade: 4
# dezenas: 3
# centenas: 8
# milhares: 1

num = int(input("Digite um número entre 0 e 9999: "))

unidade = num % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num // 1000) % 10

print("Unidade:", unidade)
print("Dezena :", dezena)
print("Centena:", centena)
print("Milhar :", milhar)
