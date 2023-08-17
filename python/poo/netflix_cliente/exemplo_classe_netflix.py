#criando uma classe para clientes Netflix

class Cliente(): #o parênteses é opcional
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium'] #planos disponíveis
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido') #cria uma exceção para que uma mensagem de erro customizada apareça

    #as funções são independentes, a variável lista_planos não poderia ser usada em outra função, mas se usar da forma "self.lista_planos", pode ser usada em qualquer outro lugar

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano inválido')


    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print('Faça upgrade para premium para ver esse filme')
        else:
            print('Plano inválido')


cliente = Cliente('Stefany','stefany@gmail.com','premium')
print(f'Cliente {cliente.plano} criado')
cliente.ver_filme('Harry Potter', 'premium')
cliente.mudar_plano('basic')
print(f'Plano alterado para {cliente.plano}')
cliente.ver_filme('Harry Potter', 'premium')