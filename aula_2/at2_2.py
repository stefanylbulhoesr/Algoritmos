'Faça um programa que receba 5 números do usuário e retorne a média aritmética'

from statistics import mean
contador = 0
numeros = []
while contador < 5:
    n = int(input("Digite um numero: "))
    numeros.append(n)
    contador = contador + 1
print(mean(numeros))
