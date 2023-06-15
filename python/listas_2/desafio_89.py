ficha = list()

while True: 
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja continuar?[S/N] '))
    if resposta in 'Nn':
        break

print(f'No   Nome      Média   ')
for i, aluno in enumerate(ficha):
    print(f'{i}   {aluno[0]}      {aluno[2]}')

while True:
    opcao = int(input('Mostrar notas de qual aluno? (Selecione um No)(999 interrompe) '))
    if opcao == 999:
        print('Fim')
        break
    if opcao <= len(ficha) -1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
