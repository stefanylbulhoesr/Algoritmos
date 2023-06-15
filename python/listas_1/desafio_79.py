lista = []
while True:
    n = int(input("Digite um número: "))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não será adicionado à lista.')
    r = str(input("Quer continuar? (s/n) "))
    if r in 'nN':
        break

lista.sort()
print(f'Você digitou os valores {lista}')