tamanhoDaArea = int(input("Digite o tamanho da area"))
print("precisa de tanto litros", tamanhoDaArea/6)
custoAreaLataode18 = 80/(6*18)
custoAreaLatinha = 25/(6*3.6)
litrosNecessarios = (tamanhoDaArea/6) * 1.1
latasdedezoito = litrosNecessarios // 18
print(litrosNecessarios,"L")
qtdSobrada = litrosNecessarios - (latasdedezoito * 18)
print(qtdSobrada)

if((qtdSobrada > 10.8) or qtdSobrada == 0):
    print("Compra so latas de 18")
    if(qtdSobrada != 0):
        print(latasdedezoito + 1)
    print("Custo total:",latasdedezoito * 80 )
elif (litrosNecessarios > 10.8):
    print("Misture")
    print(latasdedezoito, "Latas de 18")
    print(qtdSobrada // 3.6 + 1, "Latas de 3.6")
    print("Custo total:",latasdedezoito * 80 +( qtdSobrada // 3.6 + 1) * 25)
    
else:
    print("Compre somente de 3.6 litros")
    print(qtdSobrada // 3.6 + 1, "Latas de 3.6")
    print("Custo total: ", (qtdSobrada // 3.6 + 1) * 25)
