def heap(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[i] < lista[esquerda]:
        maior = esquerda

    if direita < n and lista[maior] < lista[direita]:
        maior = direita

    if maior != i:
        (lista[i], lista[maior]) = (lista[maior], lista[i])

        heap(lista, n, maior)

def heapSort(lista):
    n = len(lista)

    for i in range(n // 2 -1, -1, -1):
        heap(lista, n, i)

    for i in range(n -1, 0, -1):
        (lista[i], lista[0]) = (lista[0], lista[i])
        heap(lista, i, 0)

lista = [5, 54, 28, 10, 32, 45, 11, 13, 9]
heapSort(lista)
print(lista)