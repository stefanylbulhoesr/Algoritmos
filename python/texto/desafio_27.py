nome_completo = str(input("Digite o nome completo: ")).strip()
nomes = nome_completo.split()
print(nomes[0], nomes[len(nomes)-1]) #utiliza o len -1 para encontrar a ultima posição do array