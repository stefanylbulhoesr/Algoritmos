def quedaLivre(s = None, so = None, t = None, v = None):
    s = float(input("Qual a altura inicial?(em metros) "))
    t = ((s * 2)/-9.78) ** (1/2)
    v = (-9.78) * t
    so = s + ((9.78 * (t ** 2))) / 2
    print(f'O tempo de queda é de {t} segundos')
    print(f'A velocidade final é de {v} m/s')
    print(f'A altura final é de {so} metros')

quedaLivre()