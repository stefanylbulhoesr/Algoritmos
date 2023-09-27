def quedaLivre(s = None, a = None, t = None, v = None, vo = None):
    a = (2 * s) / (t ** 2)
    v = a * t
    t = (vo - v) / (-9.78)
    s = (v * t) - ((9.78 * (t ** 2)) / 2)
    print(a)
    print(v)
    print(t)
    print(f'A altura máxima atingida é de {s} metros')

quedaLivre(s = 12.5, t = 21.5, vo = 0)