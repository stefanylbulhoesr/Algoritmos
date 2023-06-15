valores = []
cont = 0
while True:
    n = int(input("Digite um valor: "))
    valores.append(n)
    r = str(input("Quer continuar?(s/n) "))
    if n == 5:
        cont = cont + 1
    if r in 'Nn':
        break

print(f"Foram digitados {len(valores)} números.")
valores.sort(reverse=True)
print(f"Esses foram os valores digitados em ordem decrescente: {valores}")
print(f"O número 5 foi digitado {cont} vezes ", end='')
if cont != 0:
    print(f"e, portanto, está na lista")
else:
    print(f"e, portanto, não está na lista.")