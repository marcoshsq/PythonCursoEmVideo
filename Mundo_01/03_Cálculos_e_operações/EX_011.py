# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2m²

# Cada litro (L) de tinta pinta uma área de 2m².

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura
litros_tinta = area / 2  # 1 litro cobre 2m²

print("A parede tem {:.2f} metros de largura e {:.2f} metros de altura.".format(largura, altura))
print("Área total da parede: {:.2f} m²".format(area))
print("Você precisará de {:.2f} litros de tinta para pintá-la.".format(litros_tinta))
