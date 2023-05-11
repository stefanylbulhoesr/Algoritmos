'Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números impares no vetor IMPAR. Imprima os três vetores'

numeros = []
par = []
impar = []

for i in range(0,20):
    n = int(input("Digite um número: "))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Números: {numeros}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')