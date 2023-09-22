numeros = []
resposta = "Sim"
soma = 0
while (resposta.lower() != "sair"):
    resposta=input("Deseja continuar? ")
    if(resposta.lower()=="sair"):
        break
    numero = int(input("Digite um numero entao: "))
    if(numero > 0):
        numeros.append(numero)
        soma = soma + numeros[-1]
    print("media:",soma/len(numeros))
    