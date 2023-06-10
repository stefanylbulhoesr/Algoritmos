def countingSort(lista1, max_val):
    m = max_val + 1
    cont = [0] * m                
    
    for a in lista1:
        cont[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(cont[a]):  
            lista1[i] = a
            i += 1
    return lista1

lista = [5, 54, 28, 10, 32, 45, 11, 13, 9]
countingSort(lista, 54 )
print(lista)