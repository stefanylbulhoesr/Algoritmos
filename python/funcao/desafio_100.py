from random import randint
numeros = []

def sorteia():
    for i in range(0,4):
        n = randint(1, 100)
        numeros.append(n)

sorteia()
print(f'Os números sorteados foram: {numeros}')
def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma = soma + i
    print(f'Somando os valores pares de {numeros}, temos: {soma}')
        
somapar(numeros)

