'Cálculo de fatorial'
#algoritmo    
#    inteiro, n, i, fatorial
#    n <- 5
#    fatorial <- 1
#    para i de 1 ate n faca
#        fatorial <- fatorial * i
#    fim_para
#    escreva("O fatorial de", n, "é: ", fatorial)
#fim_algoritmo

n = 5
fatorial = 1

for i in range (1,n+1):
    fatorial = fatorial * i
print("O fatorial de",n,"é:",fatorial)