lista = [5, 54, 28, 10, 32, 45, 11, 13, 9]

def bubbleSort(lista):
    for num in range(len(lista)-1, 0, -1):
        for i in range(num):
            if lista[i] > lista[i+1]:
                varTemp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = varTemp

bubbleSort(lista)
print(lista)