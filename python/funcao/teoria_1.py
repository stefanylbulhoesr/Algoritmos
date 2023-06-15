def mostralinha():
    print('------------------------------')


mostralinha()
print('     Sistema de Alunos      ')
mostralinha()

 
def mensagem(msg):
    print('------------------------------')
    print(msg)
    print('------------------------------')


mensagem('Sistema de alunos')

def soma(* valores):
    s = 0
    for num in valores:
        s+= num
    print(f'Somando os valores {valores} temos {s}')


soma(8,6)
soma(2,50)
soma(90,55)

def contador(*num): #o asterisco é o simbolo de desempacotar, pega todos os parametros e joga dentro de num
    print(num)
    tam = len(num)
    print(f'{tam} numeros')

contador(2, 1, 7)
contador(1)
contador(1,5,6,9,8,7)

def dobra(lista):
    pos = 0 
    while pos < len(lista):
        lista[pos] *=2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

