qtd = 0
numero = -1
while(numero != 0):
    numero = int(input("Digite um numero: "))
    if(numero == 0):
        break
    if(numero <= 200 and numero >= 100):
        qtd = qtd + 1
print(qtd)