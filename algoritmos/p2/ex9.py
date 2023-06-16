def alg_sort(lista): #define uma função com uma lista como parâmetro
    n = len(lista) #define uma variavel n tendo o tamanho da lista
    for i in range(n-1): #cria um loop para percorrer o tamanho da lista - 1
        for j in range(n-i-1): #cria outro loop para ir pulando de 1 em 1
            if lista[j] > lista[j+1]: #compara os valores da lista
                lista[j], lista[j+1] = lista[j+1], lista[j] #esse procedimento troca os valores de lugar, caso um valor seja maior que o outro

numeros = input("Digite a lista de números separados por espaço: ").split() #um input para definir os valores da lista, usando o slip para separar os valores
numeros = [int(num) for num in numeros] #criando a lista de numeros, usando o input anterior

alg_sort(numeros) #chamando a função

print("Lista ordenada: ", numeros) #printando a lista com os números já ordenados