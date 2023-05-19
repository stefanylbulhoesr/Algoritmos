'Calcule os 5 termos de uma Progressão Geométrica(PG) iniciando com 2 e com razão 3'
lista = []
def pg(a1,q):
    for i in range(1,6):
        an = a1 * (q**(i-1))
        lista.append(an)
    return lista

print(pg(2,3))