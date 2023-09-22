exedente = 0
multa = 4
pesodePeixes=int(input("Digite os kilo dos peixes"))
if(pesodePeixes > 50):
    excedente = pesodePeixes - 50
print("Kg pescados", pesodePeixes)
if(pesodePeixes > 50):
    print("Excedente: ", excedente)
    multa= multa * excedente
    print("Multa", multa)
else:
    print("Multa", 0)
