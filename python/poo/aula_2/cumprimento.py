def cumprimento(nome = None, idade = None):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    print(f'Olá, {nome}. Você tem {idade} anos!')

cumprimento()