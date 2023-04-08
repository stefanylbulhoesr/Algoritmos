'A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55... Faça um programa capaz de gerar a série até o n-ésimo termo.'

ant = 0
preAnt = 1
n = int(input("Qual n-ésimo termo deseja? "))
for numero in range(1,n+1):
    fib = preAnt + ant
    preAnt = ant
    ant = fib
    print(fib)
   

