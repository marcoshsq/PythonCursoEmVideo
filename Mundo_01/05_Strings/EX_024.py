# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"

cidade = input("Digite o nome de uma cidade: ").strip()

# Verifica se começa com "Santo"
comeca_com_santo = cidade[:5].lower() == "santo"

print("A cidade começa com 'Santo'? {}".format(comeca_com_santo))
