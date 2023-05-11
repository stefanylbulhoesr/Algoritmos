'Foram anotadas as idades e alturas de 30 alunos. Faça um programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos'

from statistics import mean

menorquemedia = 0
alunos = []
alturas = []

for i in range(0,30):
    altura = int(input("Altura em cm: "))
    idade = int(input("Idade: "))
    alunos.append({"altura": altura, "idade": altura})
    alturas.append(altura)

mediaAlturas = mean(alturas)

for aluno in range(0,30):
    if alunos[aluno]['altura'] < mediaAlturas and alunos[aluno]['idade'] > 13:
        menorquemedia = menorquemedia + 1

print(f'{menorquemedia} alunos com mais de 13 anos são menores do que a média de altura.')
