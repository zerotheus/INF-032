quantidadeDeFitas = int(input("informe a quantidade de fitas"))
valorDoAluguel = float(input("Informe o valor do aluguel"))
quantidadeDeFitasAlugadasPorMes = quantidadeDeFitas * (1/3)
valorFaturadoMensalSemMultas = quantidadeDeFitasAlugadasPorMes * valorDoAluguel
valorMensalGanhoComMultas = valorFaturadoMensalSemMultas * 11/10
valorGanhoSomenteComMultas = valorFaturadoMensalSemMultas * 1/10
print("Faturamento {}".format( valorMensalGanhoComMultas * 12))
print("Valor ganho com multas {}".format(valorGanhoSomenteComMultas))
print("fitas ao fim do ano {}".format(int(quantidadeDeFitas* 11/10 - (quantidadeDeFitas * 0.02))))
