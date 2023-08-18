valorEmprestimo = float(input("informe o valor do emprestimo "))
taxaDeJurosAoMes = float(input("informe o valor dos juros "))
quantidadeDemeses = float(input("Informe a quantidade de meses "))
totalAPagarAoMes = valorEmprestimo*taxaDeJurosAoMes/quantidadeDemeses
print(totalAPagarAoMes)