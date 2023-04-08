#Programa que lê as notas de um aluno e
#calcule a média, além de verificar se o aluno
#foi aprovado com base em critério de 
#nota mínima = 6.0

n1 = float(input("Digite a nota: "))
n2 = float(input("Digite a nota: "))
n3 = float(input("Digite a nota: "))

media = (n1 + n2 + n3)/3
print("A média é: %.2f" %media)

if media >=  6:
    print("Aprovado.")
else:
    print("Reprovado.")
