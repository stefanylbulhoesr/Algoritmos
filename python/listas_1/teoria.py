lista = ['hamburguer', 'pizza', 'pudim', 'cookie']
lista[1] = 'refrigerante' #adiciona item no indice 1
print(lista)
lista.append('picole') #adiciona um elemento no final da lista
print(lista)
lista.insert(0,'hotdog') #adiciona um elemento na posição definida no método
print(lista)
del lista[3] #elimina o elemento do indice definido
# lista.pop(1) faz a mesma coisa
# lista.remove('pudim') elimina o item definido
#se usar lista.pop() sem definir um elemento, o último elemento da lista será eliminado
print(lista)
#para verificar se um item está na lista, antes de removê-lo
if 'pizza' in lista:
    lista.remove('pizza')
valores1 = list(range(4,11)) #cria uma estrutura de lista ordenada
valores2 = [8, 2, 5, 4, 9, 3, 0]
print(valores2)
valores2.sort() #coloca os valores em ordem
print(valores2)
valores2.sort(reverse=True) #coloca os numeros na ordem inversa
print(valores2)
print(len(valores2)) #quantidade de elementos na lista
