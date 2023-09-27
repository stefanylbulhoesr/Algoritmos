class ContaBancaria:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = 0

    def depositar(self, valor = None):
        valor = float(input("Quanto deseja depositar? "))
        if valor > 0:
            self.saldo += valor
            print(f'O valor de {valor} foi depositado com sucesso!')
        else:
            print(f'Valor inválido!')
    
    def sacar(self, valor = None, senha = None):
            valor = float(input("Quanto deseja sacar? "))
            senha = input("Digite sua senha: ")
            if senha == self.senha:
                if valor > self.saldo:
                    print(f'Saldo insuficiente! Saque não realizado!')
                elif valor > 0 and valor <= self.saldo:
                    self.saldo -= valor
                    print(f'Saque de {valor} reais realizado com sucesso!')
            else:
                print(f'Senha inválida!')
    
    def pix(self, valor = None, senha = None):
            valor = float(input("Qual o valor do pix? "))
            senha = input("Digite sua senha: ")
            if senha == self.senha:
                if valor > self.saldo:
                    print(f'Saldo insuficiente! Pix não realizado!')
                elif valor > 0 and valor <= self.saldo:
                    self.saldo -= valor
                    print(f'Pix de {valor} reais realizado com sucesso!')
            else:
                print(f'Senha inválida!')

stefany = ContaBancaria("Stefany", 13951508779, "stefany123")
print(f'Saldo inicial: R${stefany.saldo}')
stefany.depositar()
print(f'Saldo: R${stefany.saldo}')
stefany.sacar()
print(f'Saldo: R${stefany.saldo}')
stefany.pix()
print(f'Saldo: R${stefany.saldo}')
    