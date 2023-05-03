'Crie uma string contendo uma frase e conte quantas vezes uma determinada palavra se repete'

str1 = 'Três pratos de trigo para três tigres tristes.'
contador = 0
frase = str1.split()

for i in range(0,len(frase)):
    if frase[i] == 'três' or frase[i] == 'Três':
        contador = contador + 1
print(f'Quantidade de "Três" = {contador}')