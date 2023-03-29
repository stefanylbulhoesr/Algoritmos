'Faça um programa que calcule o IMC de uma pessoa'

altura = float(input("Qual a sua altura(m)? "))
peso = float(input("Qual o seu peso(kg)? "))

imc = peso / (altura ** 2)

print("Seu IMC é: %.2f" %imc)

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif imc >= 18.5 and imc <= 24.9:
    print("Você está no peso ideal.")
elif imc >= 25 and imc <= 29.9:
    print("Você está com sobrepeso (obesidade grau I).")
elif imc >= 30 and imc <= 39.9:
    print("Você está com obesidade grau II.")
elif imc > 40:
    print("Você está com obesidade grau III.")