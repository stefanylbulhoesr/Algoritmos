'Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius'

tempFah = float(input("Digite a temperatura (em Fahrenheit): "))

tempCel = (tempFah - 32)/1.8

print("A temperatura em Celsius é %.2f" %tempCel, "º.")