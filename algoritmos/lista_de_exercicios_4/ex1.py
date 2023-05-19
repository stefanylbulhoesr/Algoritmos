'Crie uma função que calcule a média de uma lista [5, 7, 10, 3, 8]'
from statistics import mean
lista = [5, 7, 10, 3, 8]

def media(lista):
    return mean(lista)

print(media(lista))