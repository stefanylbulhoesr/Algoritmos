pessoas = []
dados = []
maior = 0
menor = 0

while True:
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] < menor:
            menor = dados[1]
        if dados[1] > maior:
            maior = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input("Quer continuar? [S/N] "))
    if r in 'Nn':
        break

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi de {maior} kg.')
for i in pessoas:
    if i[1] == maior:
        print(f'Quem tem esse peso é {i[0]}.')
print(f'O menor peso foi de {menor} kg.')    
for j in pessoas:
    if j[1] == menor:
        print(f'Quem tem esse peso é {j[0]}.')