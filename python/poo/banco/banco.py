class Cliente:
    def __init__(self, nome, idade, conta_do_banco, nome_do_banco):
        self.nome = nome
        self.idade = idade
        self.conta_do_banco = conta_do_banco
        self.nome_do_banco = nome_do_banco
        self.saldo = 0 

    def sacar(self):
        valor = float(input("Quanto deseja sacar? "))
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f'Seu saque de {valor} reais foi realizado com sucesso!')

    def depositar(self):
        valor = float(input("Quanto deseja depositar? "))
        acao = input("Insira o envelope (inserir/nao inserir): ")
        if acao == "inserir":
            self.saldo += valor
            print(f'Seu depósito de {valor} reais foi realizado com sucesso!')
        else:
            print(f'Seu depósito de {valor} reais não foi realizado!')

    @staticmethod
    def extrato():
        print(f'Seu saldo é de {cliente.saldo} reais!')


cliente = Cliente('Stefany', '27', '123456', 'Itaú')

print(f'Olá, {cliente.nome} de {cliente.idade} anos, sua conta no {cliente.nome_do_banco} é {cliente.conta_do_banco}.')
operacao = input("Qual operação deseja realizar? (deposito/saque/extrato/sair) ")
while operacao != "sair":

    if operacao == "deposito":
        cliente.depositar()
    elif operacao == "saque":
        cliente.sacar()
    elif operacao == "extrato":
        cliente.extrato()
    else:
        print("Operação inválida.")
    
    operacao = input("Qual operação deseja realizar? (deposito/saque/extrato/sair) ")

print(f'Obrigada por usar o banco {cliente.nome_do_banco}! Até logo!')
