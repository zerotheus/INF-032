nomedoMunicipio = input("Informe o nome do municipio")
qtdEleitores = int(input("Digite a quantidade de eleitores"))
if(qtdEleitores < 20000):
    print("nao tem segundo turno")
else:
    qtdDevotosDoPrimeiroColocado = int(input("Informa a quantidade de votos"))
    if((qtdDevotosDoPrimeiroColocado / qtdEleitores) < 0.5):
        print("Tem segundo turno")
    else:
        print("Nao tem segundo turno")