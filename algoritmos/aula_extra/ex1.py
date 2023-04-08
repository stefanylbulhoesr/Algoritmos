'Calcule a média de n elementos'

n = int(input("Quantos serão os elementos? "))

soma = 0

for i in range(n):
    elemento = float(input("Entre com os elementos: "))
    soma = soma + elemento

media = soma / n
print("A média dos elementos é",media)

