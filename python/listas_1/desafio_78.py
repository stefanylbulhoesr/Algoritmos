valores = []

for i in range(0,5):
    valores.append(int(input(f"Digite um valor para a posição {i}: ")))

valoresc = valores[:]
valoresd = valores[:]

print(f'Os valores digitados foram: {valores}')
valoresc.sort()
print(f'O menor valor digitado foi {valoresc[0]} na posição ', end='')
for i, valor in enumerate(valores):
    if valor == valoresc[0]:
        print(f'{i}')
valoresd.sort(reverse=True)
print(f'O maior valor digitado foi {valoresd[0]} na posição ', end='')
for i, valor in enumerate(valores):
    if valor == valoresd[0]:
        print(f'{i}')

