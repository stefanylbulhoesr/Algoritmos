#Escreva um programa que leia o valor do salário de um
#funcionário e calcule o novo salário com um aumento
#de 15%

salario = float(input("Digite o salário: "))
porcentagem = 15/100
aumento = salario * porcentagem
novosalario = salario + aumento
print("O novo salário é:",novosalario)
