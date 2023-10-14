pesoDeUmaGota = 25
idade = int(input("Informe sua idade: ")) 
peso = int(input("Informe seu peso: ")) 

if(idade >= 12):
    if(peso >= 60):
        print("Quantidade de gotas: " ,1000//pesoDeUmaGota)
    else:
        print("Quantidade de gotas: " ,875//pesoDeUmaGota)
else:
    if(5 <= peso <= 9):
        print("Quantidade de gotas: " ,125//pesoDeUmaGota)
    if(9 < peso <= 16):
        print("Quantidade de gotas: " ,250//pesoDeUmaGota)
    if(16 < peso <= 24):
        print("Quantidade de gotas: " ,375//pesoDeUmaGota)
    if(24 < peso <= 30):
        print("Quantidade de gotas: " ,500//pesoDeUmaGota)
    if(30 < peso):
        print("Quantidade de gotas: " ,750//pesoDeUmaGota)
        