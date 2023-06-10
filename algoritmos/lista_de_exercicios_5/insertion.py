def insertionSort(lista):
    for i in range(1,len(lista)):
        elemento = lista[i]
        j = i - 1
        while j >= 0 and elemento < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elemento

lista = [5, 54, 28, 10, 32, 45, 11, 13, 9]
insertionSort(lista)

print(lista)
