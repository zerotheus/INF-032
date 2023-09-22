nome = ""
nomes = []
while(nome.lower() != "fim"):
    nome = input()
    if(nome.lower() != "fim"):
        nomes.append(nome)
for firstChar in nomes:
    print(firstChar[0])