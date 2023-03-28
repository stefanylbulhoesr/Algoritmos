'Faça um programa que imprima a tabuada de um número fornecido pelo usuário'

n = int(input("Insira o número que deseja descobrir a tabuada: "))
for i in range (1,11):
   resultado = i * n
   print(n, "x", i, "=", resultado)
   