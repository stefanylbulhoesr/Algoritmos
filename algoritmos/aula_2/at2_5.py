'Faça um programa que calcule as potências de 2 até um determinado número'

n = int(input("Insira um número para descobrir sua potencia na base 2: "))

for i in range (0,n+1):
    print("2 elevado a", i, "=", 2**i)
