class Pessoa:
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf

if __name__ == "__main__":
    pessoa1 = Pessoa("Stefany", "F", "123456789")
    print(pessoa1.nome)