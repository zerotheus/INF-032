valorPorLitro = {"a":1.9,"g": 2.5}
descontoPorCombustivel = {"a":[0.97,0.95],"g": [0.96,0.94]}
combustivel = " "
while((not combustivel.startswith("a")) and (not combustivel.startswith("g"))):
    combustivel = input("Digite o tipo do combustivel")
    combustivel = combustivel.lower()
litros = float(input("Digite a quantidade de combustivel"))
if(litros < 20):
    vvl=valorPorLitro.get(combustivel[0])
    ddc =descontoPorCombustivel.get(combustivel[0])
    print(vvl)    
    print(vvl * litros * ddc[0])
else:
    vvl=valorPorLitro.get(combustivel[0])
    ddc =descontoPorCombustivel.get(combustivel[0])
    print(vvl)    
    print(vvl * litros * ddc[1])
    