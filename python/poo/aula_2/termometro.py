def termometro(temp = None):
    temp = float(input("Digite a temperatura: "))
    if temp < 37:
        print("Sem febre")
    elif temp >=37 and temp <38:
        print("Estado febril")
    elif temp >= 38:
        print("Febre")

termometro()