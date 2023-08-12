numero = 123
n1 = numero%10
numero = numero//10
n2 = numero%10
numero = numero//10
n3 = numero
numeroInvertido = n3*100 + n2*10 + n1
print(numeroInvertido)