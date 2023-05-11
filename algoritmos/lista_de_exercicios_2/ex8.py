'Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida'

idades = []
alturas = []

for i in range (0,5):
    idade = float(input("Digite a idade: "))
    altura = float(input("Digite a altura em cm: "))
    idades.append(idade)
    alturas.append(altura)
idades.reverse()
alturas.reverse()
print(idades)
print(alturas)


