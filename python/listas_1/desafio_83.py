expressao = str(input("Digite a expressão: "))
abre = expressao.count('(')
fecha = expressao.count(')')

if abre != fecha:
    print("A expressão está incorreta.")
else: 
    print("A expressão está correta.")


