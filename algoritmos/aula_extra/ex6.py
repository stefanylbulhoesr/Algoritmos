# <18 menor de idade
# >18 e <60 adulto
# >60 idoso

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade.")
elif idade >= 18 and idade <60:
    print("Adulto.")
else:
    print("Idoso.")