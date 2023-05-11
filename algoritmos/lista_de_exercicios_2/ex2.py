'Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa'

lista1 = []

for i in range (0,10):
    num = float(input("Insira um valor real: "))
    lista1.append(num)
lista1.reverse()
print(lista1)
