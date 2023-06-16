def calculaImposto(taxaImposto, custo):
    valorFinal = custo + (custo * (taxaImposto/100))
    return valorFinal

taxa = float(input("Qual o valor da taxa em %? "))
custo = float(input("Qual o valor do produto? "))

print(f'O produto custava {custo}, mas com a taxa de {taxa}%, passou a custar {calculaImposto(taxa,custo)}')