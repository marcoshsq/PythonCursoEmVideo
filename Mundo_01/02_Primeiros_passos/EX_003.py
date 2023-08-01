# Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.

num1 = int(input("Primeiro número: \n"))
num2 = int(input("Segundo número: \n"))
print("A soma é:", num1 + num2)
print("A soma é: %d!" % (num1 + num2))
print("A soma é: {}!".format(num1 + num2))

# Os três formatos de print aceitam operações entre variáveis

# Solicitar ao usuário para inserir os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calcular a soma dos números
soma = num1 + num2

# Mostrar o resultado
print(f"A soma de {num1} e {num2} é igual a {soma}")