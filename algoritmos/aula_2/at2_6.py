'Faça um programa que calcule o fatorial de um número'

n = int(input("Insira um número para descobrir seu fatorial: "))
fatorial = 1
for i in range (1,n+1):
    fatorial = fatorial * i 

print("O fatorial de", n, "é: ", fatorial)
