class Banco():
    def __init__(self, conta, usuario, senha):
        self.conta = conta
        self.usuario = usuario
        self.senha = senha

class Pessoa():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

#usando agregação, vamos criar três pessoas e cada uma terá uma conta, usando o nome das pessoas

if __name__ == "__main__":
    pessoa1 = Pessoa("Stefany", 27, "feminino")
    pessoa2 = Pessoa("Cainã", 27, "masculino")
    pessoa3 = Pessoa("Iago", 27, "masculino")

    conta1 = Banco(pessoa1.nome, "stef", "stefany123")
    conta2 = Banco(pessoa2.nome, "cain", "caina123")
    conta3 = Banco(pessoa3.nome, "iaguinho", "iago123")

    print(f'A conta {conta1.conta}, tem usuário {conta1.usuario} e senha {conta1.senha}, pertence a {pessoa1.nome}, de {pessoa1.idade} anos, do sexo {pessoa1.sexo}')
    
    print(f'A conta {conta2.conta}, tem usuário {conta2.usuario} e senha {conta2.senha}, pertence a {pessoa2.nome}, de {pessoa2.idade} anos, do sexo {pessoa2.sexo}')
    
    print(f'A conta {conta3.conta}, tem usuário {conta3.usuario} e senha {conta3.senha}, pertence a {pessoa3.nome}, de {pessoa3.idade} anos, do sexo {pessoa3.sexo}')