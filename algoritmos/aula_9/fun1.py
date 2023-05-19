import math

def soma(a,b): #def define a função e () define os parâmetros
    return a + b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a / b

def raizQuadrada(n):
    return math.sqrt(n)

def potencia(x,y):
    return x**y

def potenciaComBib(x,y):
    return math.pow(x,y)

resultadosoma = soma(14,15)
resultadomult = multiplicacao(14,15)
resultadodiv = divisao(14,15)
resultadopot = potenciaComBib(2,10)

print(resultadosoma, resultadomult, resultadodiv, resultadopot)

def calculaCaracteres(a):
    return len(a)

nCaracteres = calculaCaracteres('stefany')

print(nCaracteres)

