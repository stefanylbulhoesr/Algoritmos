

lista = []
n = int(input("Deseja uma lista de quantos números? "))
for i in range(1,n+1):
    lista.append(int(input("Digite um número: ")))

par = []
def listaPar(lista):
    for i in lista:
        if i % 2 == 0:
            par.append(i)
    return par
print(f'São pares: {listaPar(lista)}')
