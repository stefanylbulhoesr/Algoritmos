#Fatiamento - conseguir pegar pedaços de uma string
frase = 'curso em video python'
print(frase[9]) #numero do índice dentro da string, começando no 0
print(frase[9:13]) #seleciona uma cadeia entre o 9 e o 12
print(frase[9:21:2]) #vai do 9 ao 20, pulando de 2 em 2
print(frase[:5]) #quando omite o início, começa do 0
print(frase[15:]) #vai do 15 em diante
print(frase[9::3]) #vai do 9 até o final de 3 em 3
print(len(frase)) #comprimento da string
print(frase.count('o')) #conta quantas vezes aparece um caractere na string
print(frase.count('o',0,13)) #conta quantas vezes aparece o caractere de um ponto até o outro
print(frase.find('deo')) #diz em que posição começou o 'deo'
print(frase.find('android')) #quando coloca uma string que não existe, retorna o valor -1

print('curso' in frase) #verifica se existe 'curso' na cadeia de strings frase, resultando em True ou False

print(frase.replace('python', 'android')) #troca uma palavra por outra
print(frase.upper()) #coloca todas as letras maiúsculas
print(frase.upper().count('O'))

print(frase.lower()) #coloca as letras minúsculas
print(frase.capitalize()) #joga todos os caracteres para minúsculo e a primeira letra para maiúscula
print(frase.title()) #onde tem espaço, faz uma quebra de palavra e coloca a primeira letra de cada palavra maiúscula

frase1 = '   Aprenda Python  '
print(frase1.strip()) #remove os espaços inúteis da frase
print(frase1.rstrip()) #remove os espaços só da direita (right)
print(frase1.lstrip()) #remove os espaços só da esquerda (left)

print(frase.split()) #divide as strings por espaço, criando um array de strings
print('-'.join(frase)) #junta as strings por algo, nesse caso, '-'

dividido = frase.split()
print(dividido[2][3]) #o segundo índice, o terceiro dentro dele