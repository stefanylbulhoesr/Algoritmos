n = int(input("Digite um número: "))
contagem = []

def sequencia(n):
    for i in range(1,n+1):
        contagem.append(i)
        print(contagem)
    return '...'

print(sequencia(n))