sigla = input("Digite a sigla do seu estado")
sigla.capitalize

if sigla == "ZZ":
    print("sigla invalida")

if "BA" == sigla:
    print("Bahiano")
elif "SP" == sigla:
    print("Paulista")
elif "MG" == sigla:
    print("Mineiro")
else:
    print("Outros estado")