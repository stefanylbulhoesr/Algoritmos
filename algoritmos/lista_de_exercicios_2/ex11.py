'Altere o programa anterior, intercalando 3 vetores de 10 elementos cada'

lista1 = list(range(1,11))

lista2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

lista3 = list(range(11,21))

lista4 = []

for i in range(0,10):
    lista4.append(str(lista1[i]))
    lista4.append(lista2[i])
    lista4.append(str(lista3[i]))

print(lista4)