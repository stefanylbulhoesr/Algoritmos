def fatorial(n):
    if n==0 or n==1:     # caso base
        return 1      # caso base
    return n * fatorial(n-1)     # passo recursivo

#interatividade:
num = int(input('Digite um número inteiro não negativo: '))

resultado = fatorial(num)

print('O fatorial de ', num, ' é ', resultado)
