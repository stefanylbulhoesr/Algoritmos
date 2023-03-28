'Faça um programa que leia um número inteiro e exiba se ele é par ou ímpar'

n = int(input("Digite um número inteiro para descobrir se é par ou ímpar: "))
if n % 2 == 0:
    print("O número", n, "é par.")
else:
    print("O número", n, "é ímpar.")