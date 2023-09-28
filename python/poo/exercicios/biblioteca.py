#2. Fazer um sistema de biblioteca (Deve imprimir 
# uma lista com 5 livros, pedir o nome do solicitante 
# do empréstimo, pedir para selecionar um livro e 
# imprimir o livro selecionado)-Criar usando classes

class Biblioteca:
    def __init__(self, livro, solicitante):
        self.livro = livro
        self.solicitante = solicitante

class Solicitante:
    def __init__(self, nome, escola):
        self.nome = nome
        self.escola = escola

livro_0 = "Livro A"
livro_1 = "Livro B"
livro_2 = "Livro C"
livro_3 = "Livro D"
livro_4 = "Livro E"

lista_livros = [livro_0, livro_1, livro_2, livro_3, livro_4]

print("Olá, esses são os livros que temos disponíveis:")
print("[0] Livro A")
print("[1] Livro B")
print("[2] Livro C")
print("[3] Livro D")
print("[4] Livro E")

opcao = int(input("Qual o número do livro que deseja? "))
nome = input("Qual o seu nome? ")
escola = input("De qual escola é? ")

if __name__ == "__main__":
    aluno1 = Solicitante(nome, escola)
    solicitacao = Biblioteca(lista_livros[opcao], aluno1.nome)
    print(f'Solicitação feita por {solicitacao.solicitante} realizada com sucesso. {solicitacao.livro} emprestado até a próxima semana.')


