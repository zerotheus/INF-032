numero = 0
qtd = 0
while (True and numero >= 0):
    numero =int(input("Digite um numero: "))
    print(numero)
    if(numero<0):
        break
    qtd = qtd + 1
    print("Digite qualuqer numero menor que 0 pra sair")
print("Quantidade", qtd)