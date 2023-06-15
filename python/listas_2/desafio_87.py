matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

somapar = 0 
somater = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input("Digite um valor: "))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar = somapar + matriz[linha][coluna]
    print()

for linha in range(0,3):
    somater = somater + matriz[linha][2]

print(f'A soma dos pares é {somapar}.')
print(f'O maior valor da segunha linha é {max(matriz[1])}.')
print(f'A soma dos elementos da terceira coluna é {somater}.')
