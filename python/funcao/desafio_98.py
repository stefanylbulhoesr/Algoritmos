def contador(inicio, fim, passo):
    if inicio < fim:
        for cont in range(inicio,fim+1, passo):
            print(cont)
    elif inicio > fim:
        for cont in range(inicio,fim-2, -passo):
            print(cont)

contador(1, 10, 1)
contador(10, 0, 2)

x = int(input("Início: "))
y = int(input("Fim: "))
z = int(input("Passo: "))
contador(x,y,z)

