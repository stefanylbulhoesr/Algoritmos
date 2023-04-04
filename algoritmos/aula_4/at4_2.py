'Um funcionário de uma empresa recebe um aumento salarial anualmente. Saba-se que:'
'1. Esse funcionário foi contratado em 2005, com salário inicial de R$ 1000'
'2. Em 2006 recebeu aumento de 1,5% sobre seu salário inicial'
'3. A partir de 2007 (inclusive), ou aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.'
'Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário'

contrato = str(input("Utiliza salário reajustado ou salário inicial (reajustado/inicial)? "))

salIn = float(input("Qual o salário inicial? "))
porc = (15 / 1000)
if contrato == "inicial":
    for i in range (1,18):
        sal = salIn + salIn * porc 
        print(porc)
        porc = porc * 2
        print(sal)
elif contrato == "reajustado":
    for i in range (1,18):
        sal = salIn + salIn * porc 
        print(porc)
        porc = porc * 2
        print(sal)
        salIn = sal    
