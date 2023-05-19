'Crie uma função que calcula as raizes de uma equação quadrática usando a fórmula de Bhaskara'
import math

def raiz1(a,b,c):
    delta = ((b ** 2) -4 * a * c)
    raizq = (delta) ** (1/2)
    return (-b + raizq) / (2 * a)

def raiz2(a,b,c):
    delta = ((b ** 2) -4 * a * c)
    raizq = (delta) ** (1/2)
    return (-b - raizq) / (2 * a)  

print(f'Raiz 1 = {raiz1(-2,3,5)} Raiz 2 = {raiz2(-2,3,5)}')