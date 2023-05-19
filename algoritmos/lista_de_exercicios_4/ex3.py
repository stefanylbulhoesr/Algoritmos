'Calcule os 5 termos de uma Progressão Aritmética(PA) iniciando em 2 e com razão 3'
lista = []
def pa(a,r):
    lista.append(a)
    for i in range(1,5):
        lista.append(a + (r *i))
    return lista
print(pa(2,3))