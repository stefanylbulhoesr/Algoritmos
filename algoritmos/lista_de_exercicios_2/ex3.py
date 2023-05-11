'Faça um programa que leia 4 notas, mostre as notas e a média na tela'

from statistics import mean

notas = []

for i in range (0,4):
    nota = float(input("Digite a nota: "))
    notas.append(nota)
print(notas)
print(mean(notas))