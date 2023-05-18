numero = int(input("Insira um número: "))

def pos_neg(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

print(pos_neg(numero))