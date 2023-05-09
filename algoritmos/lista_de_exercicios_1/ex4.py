'Crie uma string contendo uma frase e conte quantas vezes uma determinada letra aparece na frase'

str1 = 'O rato roeu a roupa do rei de Roma'
contador = 0
for i in range(0,len(str1)):
    if str1[i] == 'r' or str1[i] == 'R':
        contador = contador + 1
print(f'r= {contador}')