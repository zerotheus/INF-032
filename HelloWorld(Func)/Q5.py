def somaImposto(taxaImposto,custo):
  taxaImposto = 1+taxaImposto/100
  custo= custo* taxaImposto
  return custo

while(True):
  print(somaImposto(int(input("Digite a porcentagem da taxa")), float(input("Digite o valor do produto"))))