#Escreva um programa que leia dois numeros inteiros
#e exiba na tela o maior deles

n1 = int(input("Entre com um valor: "))

n2 = int(input("Entre com um valor: "))
if n1 > n2:
    print("O maior é:", n1)
elif n1 == n2:
    print("Os números são iguais")
else:
    print("O maior é:", n2)