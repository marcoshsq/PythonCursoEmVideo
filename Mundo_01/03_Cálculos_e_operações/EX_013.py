# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input("Digite o salário do funcionário: R$ "))

aumento = salario * 0.15
novo_salario = salario + aumento

print("O salário era R${:.2f}, com 15% de aumento passa a ser R${:.2f}".format(salario, novo_salario))
