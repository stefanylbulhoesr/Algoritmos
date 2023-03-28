'Faça um programa que receba um número e determine se ele é primo ou não'

n = int(input("Digite um número e descubra se ele é primo: "))
contagem = 0
for contador in range (2,n):
    if (n % contador == 0):
        contagem += 1

if contagem == 0:
    print("Este número é primo.")
else:
    print("Este número não é primo.")
    