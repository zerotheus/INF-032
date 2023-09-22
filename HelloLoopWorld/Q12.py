tamanhoDaArea = int(input("Digite o tamanho da area"))
print("precisa de tanto litros", tamanhoDaArea/6)
custoAreaLataode18 = 80/(6*18)
custoAreaLatinha = 25/(6*3.6)
print("custoAreaLataode18 = ", (6*18)/80)
print("custoAreaLatinha = ",(6*3.6)/25)
litrosNecessarios = tamanhoDaArea/6
latasdedezoito = litrosNecessarios // 18
print(litrosNecessarios)
qtdSobrada = litrosNecessarios - (latasdedezoito * 18)

if((18 - qtdSobrada) > (10.8 - qtdSobrada)):
    print("Compra so latas de 18")
    print(latasdedezoito + 1)
else:
    print(qtdSobrada // 3,6 + 1)

