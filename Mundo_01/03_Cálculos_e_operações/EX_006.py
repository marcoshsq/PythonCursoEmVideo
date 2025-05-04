# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:

num = float(input("Digite um número: "))

dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** 0.5  # ou usar pow(num, 0.5)

print("O dobro de {} é {}".format(num, dobro))
print("O triplo de {} é {}".format(num, triplo))
print("A raiz quadrada de {} é {}".format(num, raiz_quadrada))
