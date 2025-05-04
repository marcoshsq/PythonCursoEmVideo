# Crie um programa que leia o nome completo de uma pessoa e faça as seguintes transformações:

nome = input("Digite seu nome completo: ").strip()

# Nome em maiúsculas
print("Nome em maiúsculas:", nome.upper())

# Nome em minúsculas
print("Nome em minúsculas:", nome.lower())

# Número de letras (sem espaços)
letras_total = len(nome.replace(" ", ""))
print("Total de letras (sem contar espaços):", letras_total)

# Letras do primeiro nome
primeiro_nome = nome.split()[0]
print("Quantidade de letras no primeiro nome:", len(primeiro_nome))
