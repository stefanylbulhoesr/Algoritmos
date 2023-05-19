def horaMinuto(hora,minuto):
    if hora < 12 and hora >0:
        return f'{hora} : {minuto} A.M'
    elif hora == 0 or hora == 00:
        return f'12 : {minuto} A.M'
    elif hora == 12:
        return f'12 : {minuto} P.M'
    else:
        return f'{hora - 12 } : {minuto} P.M'

print("Digite '100' para sair")
while True:

    hora = int(input("Insira a hora: "))
    minuto = int(input("Insira o minuto: "))
   
    if hora == 100 or minuto == 100:
        break
    print(horaMinuto(hora,minuto))
    
