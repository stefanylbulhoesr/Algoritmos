frase = str(input("Digite uma frase: ")).lower().strip() #strip tira os espaços indesejados
print("A letra 'a' aparece ", frase.count('a'), "vezes.")
print("Ela aparece pela primeira vez na posição", frase.find('a')+1)
print("A última letra 'a' aparece na posição", frase.rfind('a')+1) #procura a partir do lado direito

