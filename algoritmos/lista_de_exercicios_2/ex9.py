'Faça um programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor'

A = []
naoquadrado = []

for i in range(0,10):
    n = int(input("Digite um número: "))
    A.append(n)
    naoquadrado.append(n ** 2)

print(f'A soma dos quadrados de {A} é: {sum(naoquadrado)}')

