import math
qtd = 10
numeros = []
while(qtd>0):
    numero = int(input("Digite um numero: "))
    if(numero> 0):
        qtd = qtd - 1
        numeros.append(numero)
for umNumero in numeros:
    print(math.sqrt(umNumero))