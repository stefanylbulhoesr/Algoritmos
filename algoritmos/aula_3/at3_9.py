'Faça um programa tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: '
'a) Para homens: (72.7 * h) - 58'
'b) Para mulheres: (62.1 * h) - 44.7'

h = float(input("Qual a sua altura (m)? "))
sexo = str(input("Qual o seu sexo (h/m)? "))

if sexo == "h":
    print("Seu peso ideal é:%.2f" %((72.7 * h) - 58))
elif sexo == "m":
    print("Seu peso ideal é:%.2f" %((62.1 * h) - 44.7))
else:
    print("Escolha entre h (homem) ou m (mulher).")