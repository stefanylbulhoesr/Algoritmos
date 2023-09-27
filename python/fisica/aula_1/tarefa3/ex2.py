def quedaLivre(vo = None, t = None, s = None):
    t = vo / 9.78
    s = (vo * t) - ((9.78 * (t ** 2)) / 2)
    print(f'A bola leva {t} segundos para atingir o ponto mais alto')
    print(f'A altura máxima que a bola sobe é de {s} metros.')

quedaLivre(vo = 25.5)