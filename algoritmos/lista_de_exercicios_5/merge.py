def mergeSort(lista):
    if len(lista)>1:
        mid = len(lista)//2
        esquerda = lista[:mid]
        direita = lista[mid:]

        mergeSort(esquerda)
        mergeSort(direita)

        i=0
        j=0
        k=0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k]=esquerda[i]
                i=i+1
            else:
                lista[k]=direita[j]
                j=j+1
            k=k+1

        while i < len(esquerda):
            lista[k]=esquerda[i]
            i=i+1
            k=k+1

        while j < len(direita):
            lista[k]=direita[j]
            j=j+1
            k=k+1

lista = [5, 54, 28, 10, 32, 45, 11, 13, 9]
mergeSort(lista)
print(lista)
