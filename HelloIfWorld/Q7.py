n1 = int(input("Digite um numero "))
n2 = int(input("Digite um numero "))
n3 = int(input("Digite um numero "))

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        intermediario = n2
        menor = n3
        print(n1, n2, n3)
    else:
        intermediario = n3
        menor = n2
        print(n1, n3,n2)
elif n2 > n3:
    maior = n2
    if n1 > n3:
        intermediario = n1
        menor = n3
        print(n2, n1, n3)
    else:
        intermediario = n3
        menor = n1
        print(n2 ,n3,n1)
else:
    maior = n3
    if n1 > n2:
        intermediario = n1
        menor = n2
        print(n3,n1, n2)
    else:
        intermediario = n1
        menor = n3
        print(n3, n2,n1)