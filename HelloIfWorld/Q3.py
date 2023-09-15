sigla = input("Digite a sigla do seu estado")

if sigla.islower:
    sigla.capitalize


siglasDosEstado = [
"AC",
"AL",
"AP",
"AM",
"BA",
"CE",
"DF",
"ES",
"GO",
"MA",
"MS",
"MT",
"MG",
"PA",
"PB",
"PR",
"PE",
"PI",
"RJ",
"RN",
"RS",
"RO",
"RR",
"SC",
"SP",
"SE",
"TO"
]

if sigla == "ZZ":
    print("sigla invalida")

if "BA" == sigla:
    print("Bahiano")
elif "SP" == sigla:
    print("Paulista")
elif "MG" == sigla:
    print("Mineiro")
elif "RJ" == sigla:
    print("Carioca")
elif sigla not in siglasDosEstado:
    print("Outros estado")