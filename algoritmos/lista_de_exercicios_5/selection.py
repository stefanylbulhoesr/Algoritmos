lista1 = [5, 54, 28, 10, 32, 45, 11, 13, 9]
tamanho = len(lista1)

def selectionSort(lista,tamanhoLista):
    for passo in range(tamanhoLista):
        numMin = passo
        for i in range(passo+1,tamanhoLista):
            if lista[i] < lista[numMin]:
                numMin = i
                
        (lista[passo], lista[numMin]) = (lista[numMin], lista[passo])

selectionSort(lista1,tamanho)
print(lista1)