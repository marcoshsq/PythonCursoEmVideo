# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = input("Digite o nome completo: ").strip()

tem_silva = "silva" in nome.lower()

print("O nome tem 'Silva'? {}".format(tem_silva))
