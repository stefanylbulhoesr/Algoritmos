'Faça um programa que imprima os números de 1 a 10 usando for e while'

escolha = input("Escolha como deseja contar (while/for): ")
if escolha == "for":

    for i in range (1,11):
        print(i)
elif escolha == "while": 
    n = 0
    while n < 10:
        n = n + 1
        print (n)
