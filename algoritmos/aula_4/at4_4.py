'Sendo h = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n'
'Faça um programa que calcule o valor de h com n termos'
n = int(input("Qual o valor de n? "))
soma = 0
for n in range (1, n+1):
    frac = 1 / n
    print("1 /",n,"=",frac, "+")
    soma = frac + soma
print("h = ",soma)