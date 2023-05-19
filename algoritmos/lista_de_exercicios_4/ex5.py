'Calcule todas as permutações dos elementos de um conjunto com 3 elementos, considere uma lista = [1,2,3] OBS: Pesquise sobre itertools e permutations'
import itertools 
lista = [1,2,3]

def permutations(a,b):
    permutation = list(itertools.permutations(a,b))
    return permutation
print(permutations(lista,3))

