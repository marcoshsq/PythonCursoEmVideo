# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input("Digite o preço do produto: R$ "))

desconto = preco * 0.05
novo_preco = preco - desconto

print("O produto que custava R${:.2f}, com 5% de desconto passa a custar R${:.2f}".format(preco, novo_preco))
