'''A empresa BPVDoM resolveu dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono. Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
    *Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro
    *O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima.
    *Ao final, o programa deverá apresentar:
        - O salário de cada funcionário, juntamente com o valor do abono;
        - O número de total de funcionários processados;
        - O valor total a ser gasto com o pagamento do abono;
        - O número de funcionários que receberá o valor mínimo de 100 reais;
        - O maior valor pago como abono.'''

salarios = []
abonos = []
abonosmin = 0

while (True):
    valorsalario = float(input("Digite o valor do salário de dezembro: "))
    if valorsalario == 0:
        break
    if (valorsalario*0.2) <= 100:
        abonos.append(100)
        abonosmin = abonosmin + 1
    else:
        abonos.append(valorsalario*0.2)
    salarios.append(valorsalario)

print(f'Projeção de Gastos com Abono\n=====================\n')

for i in range(len(salarios)):
    print(f'Salário: {salarios[i]}\n')

print('Salário      -  Abono')
for a in range(len(salarios)):
    print(f'R$ {salarios[a]} - R$ {abonos[a]}\n')
print(f'Foram processados {len(salarios)} colaboradores \nTotal gasto com abonos: R$ {sum(abonos)}\nValor mínimo pago a {abonosmin} colaboradores\nMaior valor de abono pago: R$ {max(abonos)} ')