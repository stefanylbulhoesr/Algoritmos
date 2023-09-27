def MRUV(v=None, s=None, vo=None, so=None, t=None, a=None):
    vo = float(input("Qual a velocidade inicial?(em m/s) "))
    so = float(input("Qual a posição inicial?(em metros) "))
    t = float(input("Qual o tempo?(em segundos) "))
    a = float(input("Qual a aceleração?(em m/s²) "))
    v = vo + (a * t)
    s = so + (vo * t) + ((a * (t ** 2))/2)
    print(f'A velocidade final é de {v} m/s')
    print(f'A posição final é de {s} m')

MRUV()