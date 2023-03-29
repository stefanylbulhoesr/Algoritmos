'Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:'
'a) o produto do dobro do primeiro com metade do segundo'
'b) A soma do triplo do primeiro com o terceiro'
'c) O terceiro elevado ao cubo'

int1 = int(input("Insira um número inteiro: "))
int2 = int(input("Insira um número inteiro: "))
real1 = float(input("Insira um número real: "))

a = (int1 * 2) * (int2 / 2)
b = (int1 * 3) + real1
c = real1 ** 3

print("O produto do dobro do primeiro com metade do segundo é:", a)
print("A soma do triplo do primeiro com o terceiro é:", b)
print("O terceiro elevado ao cubo é:", c)
