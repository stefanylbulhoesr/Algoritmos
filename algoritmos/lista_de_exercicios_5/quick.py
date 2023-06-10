def quickSort(lista):
   quickSortHelper(lista,0,len(lista)-1)

def quickSortHelper(lista,primeiro,ultimo):
   if primeiro < ultimo:

       separacao = particao(lista,primeiro,ultimo)

       quickSortHelper(lista,primeiro,separacao-1)
       quickSortHelper(lista,separacao+1,ultimo)


def particao(lista,primeiro,ultimo):
   pivo = lista[primeiro]

   esquerda = primeiro + 1
   direita = ultimo

   pronto = False
   while not pronto:

       while esquerda <= direita and lista[esquerda] <= pivo:
           esquerda = esquerda + 1

       while lista[direita] >= pivo and direita >= esquerda:
           direita = direita - 1

       if direita < esquerda:
           pronto = True
       else:
           temp = lista[esquerda]
           lista[esquerda] = lista[direita]
           lista[direita] = temp

   temp = lista[primeiro]
   lista[primeiro] = lista[direita]
   lista[direita] = temp


   return direita

lista = [5, 54, 28, 10, 32, 45, 11, 13, 9]
quickSort(lista)
print(lista)