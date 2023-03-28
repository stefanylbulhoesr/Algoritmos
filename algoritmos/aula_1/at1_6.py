'Faça um programa que leia três números e exiba o menor deles'

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1<n2 and n1<n3:
    print("O menor número é", n1)
elif n2<n1 and n2<n3:
    print("O menor número é", n2)
elif n3<n2 and n3<n1:
    print("O menor número é", n3)

numeros = []
contador = 0
while contador < 3:
    n = int(input("Digite um numero: "))
    numeros.append(n)
    contador = contador + 1
print("O menor numero é: ", min(numeros))