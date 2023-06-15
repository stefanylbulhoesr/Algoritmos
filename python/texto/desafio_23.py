numero = int(input("Digite um número entre 0 e 9999: "))
unidade = (numero) / 1 % 10
dezena = (numero) / 10 % 10
centena = (numero) / 100 % 10
milhar = (numero) / 1000 % 10
print(f'Unidade: {int(unidade)}')
print(f'Dezena: {int(dezena)}')
print(f'Centena: {int(centena)}')
print(f'Milhar: {int(milhar)}')
