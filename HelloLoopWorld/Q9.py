map = {1: [],2: [],3: []}
costMap = {1: 0.3,2: 0.5,3: 0.7}
while(True):
    numeroDoConsumidor = int(input("Informe o numero do consumidor"))
    if(numeroDoConsumidor == 0):
        break
    kwPorHoraConsumidor = int(input("Informe os Kw/h consumidos"))
    tipoDeConsumidor = int(input("Informe o tipo do consumidor"))
    if(tipoDeConsumidor > 0 and tipoDeConsumidor < 4):
        listaDoTipo = map.get(tipoDeConsumidor)
        listaDoTipo.append(kwPorHoraConsumidor)
    else:
        print("tipo invalido")
print(map)
custoTotal = 0
mediaTipoUmEDois = 0
for i in range (1,4):
    vetor = map.get(i)
    for consumo in vetor:
        custo = consumo * costMap.get(i)
        custoTotal = custoTotal + custo
        print("Custo do consumidor:",custo)
        if(i<3):
            mediaTipoUmEDois = consumo + mediaTipoUmEDois
        continue
    i = i + 1
    continue
print("Custo total:",custoTotal)
print("Media tipo 1 e 2:", mediaTipoUmEDois/(int(len(map.get(1)))+int(len(map.get(2)))))