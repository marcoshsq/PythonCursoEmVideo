# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Último: Souza

nome = input("Digite seu nome completo: ").strip()

partes = nome.split()

primeiro = partes[0]
ultimo = partes[-1]

print("Primeiro nome:", primeiro)
print("Último nome:", ultimo)
