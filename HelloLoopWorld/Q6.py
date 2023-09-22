numeros = []
numero = 0
while(numero != 999):
    numero = int(input("Digite numero"))
    numeros.append(numero)
for umNumero in numeros:
    print("Divisores de", umNumero)
    print(umNumero)
    for i in range (1, int(umNumero/2 +1)):
        i = i + 1
        if(umNumero % int(i) == 0):
            print(i)
