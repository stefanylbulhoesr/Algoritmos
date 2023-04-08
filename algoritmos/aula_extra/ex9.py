# fibonacci
# 1,1,2,3,5,8...
# x y
# n = -2 entrada inválida

n = int(input("Digite a quantidade: "))

if n <=0:
    print("Entrada inválida")
else:
    x = 0
    y = 1
    print("A sequência até a entrada",n,"é")
    print(x)
    print(y)
    for _ in range (n-2):
        x,y = y, x+y
        print(y)