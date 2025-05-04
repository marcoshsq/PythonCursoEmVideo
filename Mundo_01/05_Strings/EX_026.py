# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input("Digite uma frase: ").strip().lower()

quantidade_a = frase.count('a')
primeira_pos = frase.find('a')
ultima_pos = frase.rfind('a')

print("A letra 'a' aparece {} vezes.".format(quantidade_a))
print("Ela aparece pela primeira vez na posição {}.".format(primeira_pos + 1))
print("Ela aparece pela última vez na posição {}.".format(ultima_pos + 1))
