#help(print) #posso usar o comando help() para descobrir como utilizar determinada função

def somar(a=0, b=0, c=0): #faz com que os parâmetros sejam opcionais
    s = a + b + c
    print(f'A soma vale {s}')

somar(5,9,500)