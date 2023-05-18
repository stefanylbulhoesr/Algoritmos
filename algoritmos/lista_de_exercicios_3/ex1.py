n = int(input("Digite um número: "))

def sequencia(n):
    for i in range(1,n+1):
        linha = (str(i) + " ") * i
        print(linha)
    return '...'

print(sequencia(n))