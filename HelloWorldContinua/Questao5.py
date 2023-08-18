kmPorLitro = 12
tempoGasto = int(input("informe o tempo"))
velocidadeMedia = int(input("informa a velocidade media"))
distancia = velocidadeMedia * tempoGasto
litrosGastos = distancia/kmPorLitro
output = "Tempo gasto {} + velocidade meida {} distancia pecorrida {} litros consumidos {}"
print(output.format(tempoGasto, velocidadeMedia, distancia, litrosGastos))