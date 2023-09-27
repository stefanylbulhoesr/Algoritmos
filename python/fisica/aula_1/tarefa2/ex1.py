def distVelTemp (distI = None, distF = None, vel = None, tempI = None, tempF = None):
    distI = float(input("Qual a distância inicial?(em metros) "))
    distF = float(input("Qual a distância final?(em metros) "))
    tempI = float(input("Qual o tempo inicial?(em segundos) "))
    tempF = float(input("Qual o tempo final?(em segundos) "))
    vel = (distF - distI) / (tempF - tempI)
    print(f'A velocidade é de {vel} m/s')


distVelTemp()
