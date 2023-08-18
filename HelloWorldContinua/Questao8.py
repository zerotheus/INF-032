numeroDeConta = int(input("informe o seu numero de conta "))
copiaDoNumeroDeConta= numeroDeConta
ultimoDigito = numeroDeConta%10
copiaDoNumeroDeConta=copiaDoNumeroDeConta//10
segundoDigito = copiaDoNumeroDeConta % 10
copiaDoNumeroDeConta = copiaDoNumeroDeConta // 10
primeiroDigito = copiaDoNumeroDeConta
numeroDeContaInvertido = ultimoDigito * 100 + segundoDigito * 10 + primeiroDigito
print(numeroDeContaInvertido)
numerodeCalculo = numeroDeContaInvertido + numeroDeConta
print(numerodeCalculo)
terceiroDigito = numerodeCalculo%10
numerodeCalculo= numerodeCalculo//10
segundoDigito = numerodeCalculo%10
numerodeCalculo = numerodeCalculo//10
primeiroDigito = numerodeCalculo
print("Digito Verificador {}".format((primeiroDigito + segundoDigito * 2 + terceiroDigito * 3)%10))