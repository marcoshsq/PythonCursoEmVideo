# Conversor de temperaturas: escreva um programa que converta uma temperatura digitada em ºC para ºF

celsius = float(input("Digite a temperatura em ºC: "))

fahrenheit = (celsius * 9 / 5) + 32

print("A temperatura de {:.1f}ºC corresponde a {:.1f}ºF.".format(celsius, fahrenheit))
