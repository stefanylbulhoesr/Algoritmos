class Amigo():
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
    
class Inimigo():
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade


if __name__ == "__main__":
    amigo1 = Amigo("Iago", 27, "Alvorada")
    amigo2 = Amigo("Cainã", 27, "Saquarema")
    amigo3 = Amigo("Kelvin", 27, "Criciúma")
    examigo = Inimigo(amigo1.nome, amigo1.idade, amigo1.cidade) #Agregação
    print(f'Meus amigos eram {amigo1.nome}, de {amigo1.idade} anos de idade, que mora em {amigo1.cidade}, {amigo2.nome}, de {amigo2.idade} anos de idade, que mora em {amigo2.cidade} e {amigo3.nome}, de {amigo3.idade} anos de idade, que mora em {amigo3.cidade}')
    print(f'Agora, eu tenho um ex-amigo, que é {examigo.nome}, de {examigo.idade} anos de idade, que mora em {examigo.cidade}')