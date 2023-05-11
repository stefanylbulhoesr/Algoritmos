'Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores'

lista1 = list(range(1,11))

lista2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

lista3 = []

for i in range(0,10):
    lista3.append(str(lista1[i]))
    lista3.append(lista2[i])

print(lista3)
    