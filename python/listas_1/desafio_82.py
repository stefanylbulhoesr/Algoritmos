lista = []
pares = []
impares = []

while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    r = str(input("Quer continuar?(s/n) "))
    if r in 'Nn':
        break
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'A lista gerada foi: {lista}')
print(f'Os pares da lista são: {pares}')
print(f'Os ímpares da lista são: {impares}')