texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.'

x = str(input("Qual letra deseja encontrar? "))
texto.lower()
quantidade = texto.count(x)
print(f'A letra {x} aparece {quantidade} vezes')
