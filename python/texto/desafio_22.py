nome = str(input("Digite o nome: "))
print(nome.upper())
print(nome.lower())
espacos = nome.count(' ')
caracteres = len(nome)
total = caracteres - espacos
print(total)
nomes = nome.split()
print(len(nomes[0]))