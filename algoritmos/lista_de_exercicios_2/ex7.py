'Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números'

from math import prod

n = []

for i in range(0,5):
    numero = int(input("Digite um número: "))
    n.append(numero)

print(f'Os números são: {n}. Sua soma é: {sum(n)}. Sua multiplicação é: {prod(n)}')