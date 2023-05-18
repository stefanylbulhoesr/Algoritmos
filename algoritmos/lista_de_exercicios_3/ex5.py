taxa = float(input("Digite o valor do imposto em %: "))
valor = float(input("Digite o valor do produto antes da tributação: ")) 
def somaImposto(taxaImposto,custo):
    valorfinal = valor - valor * (taxa/100)
    return valorfinal

print(somaImposto(taxa,valor))