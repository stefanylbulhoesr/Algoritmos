class Author():
    def __init__(self, name):
        self.name = name

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

if __name__ == "__main__": #teste do tipo de código que está usando, para verificar se ele está sendo chamado dentro desse código ou fora
    author = Author("Stefany")
    book = Book("Querido diario otario", author.name)
    print(f'O nome do livro de autor {book.author} é {book.title}')
