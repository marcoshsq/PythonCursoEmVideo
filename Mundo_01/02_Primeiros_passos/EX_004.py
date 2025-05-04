# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

dado = input("Digite algo: ")

print("O tipo primitivo desse valor é", type(dado))
print("Só tem espaços?", dado.isspace())
print("É um número?", dado.isnumeric())
print("É alfabético?", dado.isalpha())
print("É alfanumérico?", dado.isalnum())
print("Está em maiúsculas?", dado.isupper())
print("Está em minúsculas?", dado.islower())
print("Está capitalizada?", dado.istitle())
