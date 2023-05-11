'Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes'

lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

vogais = ['a', 'e', 'i', 'o', 'u']

consoantes = list(set(lista1) - set(vogais))

print(f'São {len(consoantes)} consoantes')
print(consoantes)