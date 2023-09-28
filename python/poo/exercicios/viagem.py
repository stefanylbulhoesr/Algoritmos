class Viagem:
    def __init__(self, destino, viajante):
        self.destino = destino
        self.viajante = viajante
    
lugar = int(input("Para onde deseja viajar? [0] Saquarema, [1] Maricá, [2] Vassouras"))
nome = input("Qual o seu nome? ")

lugar_0 = "Saquarema"
lugar_1 = "Maricá"
lugar_2 = "Vassouras"

lista_lugares = [lugar_0, lugar_1, lugar_2]
opcao = int(lugar)
viajante1 = Viagem(lista_lugares[lugar], nome)
print(f'{viajante1.viajante} está viajando para {viajante1.destino}')