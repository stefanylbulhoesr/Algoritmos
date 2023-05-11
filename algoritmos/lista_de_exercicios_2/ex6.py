'Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0'

mediamaiorque7 = []
mediamenorque7 = []

for i in range(0,10):
    aluno = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    if media >= 7:
        mediamaiorque7.append(media)
    else: 
        mediamenorque7.append(media)

print(f'{len(mediamaiorque7)} alunos ficaram acima da média 7.')
