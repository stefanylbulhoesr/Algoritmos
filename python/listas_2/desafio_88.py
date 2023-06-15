from random import randint
lista = []
jogos = []
resposta = int(input("Quantos jogos deseja fazer? "))

for i in range(1,resposta+1): 
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
        if len(lista) == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print(jogos)

