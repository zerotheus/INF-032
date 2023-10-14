perguntas = {}
respostas = {}
perguntas[1] = "Telefonou para a vítima?"
perguntas[2] = "Esteve no local do crime?"
perguntas[3] = "Mora perto da vítima?"
perguntas[4] = "Devia para a vítima?"
perguntas[5] = "Já trabalhou com a vítima?"
print(perguntas)
quantidadedeSim = 0
for i in range(1,6):
    print(perguntas.get(i))
    respostas[i] = input("Informe sua resposta: ")
    if(respostas.get(i).lower() == "sim"):
        quantidadedeSim = quantidadedeSim + 1
if(quantidadedeSim < 2):
    print("Inocente")
if(2 == quantidadedeSim ):
    print("Suspeita")
if(3 == quantidadedeSim or 4 == quantidadedeSim ):
    print("Cumplice")
if(5 == quantidadedeSim ):
    print("Assasino")