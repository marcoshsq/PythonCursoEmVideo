# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere R$ 3.27 = US$ 1

reais = float(input("Quanto dinheiro você tem na carteira? R$ "))

cotacao_dolar = 3.27
dolares = reais / cotacao_dolar

print("Com R${:.2f} você pode comprar US${:.2f}".format(reais, dolares))
