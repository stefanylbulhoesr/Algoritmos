dados = []
dado = list()
for i in range(0,4):
    dado.append(str(input("Digite o nome: ")))
    dado.append(int(input("Digite a idade: ")))
    dados.append(dado[:])
    dado.clear() #limpa os dados em 'dado', para que seja feita uma nova lista

totmai = 0
totmen = 0
for j in dados:
    if j[1] >= 18:
        print(f'{j[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{j[0]} é menor de idade')
        totmen += 1

print(f'{totmai} pessoas são maiores de idade e {totmen} pessoas são menores de idade')
