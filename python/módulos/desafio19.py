import random
alunos = []
for i in range(1,5):
    aluno = str(input("Digite o nome do aluno: "))
    alunos.append(aluno)

escolhido = random.choice(alunos)
print(escolhido)

random.shuffle(alunos)
print(alunos)