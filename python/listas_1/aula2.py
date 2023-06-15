valores = []
for i in range(0,5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')

a = [2, 3, 4, 7]
b = a[:] #cria uma cópia, se usar 'b=a' cria uma ligação entre as duas listas, fazendo com que uma modificação em uma também modifique a outra
b[2] = 5
print(a)
print(b) 