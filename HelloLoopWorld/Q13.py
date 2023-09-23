kilos=0
tipo =0
nomedascarnes = {1:"file",2:"Alcatra",3:"Picanha"}
tabelaDePrecos = {1:[4.9,5.8],2:[5.9,6.8],3:[6.9,7.8]}
resposta = ""
while(tipo != 1 and tipo != 2 and tipo != 3):
    tipo = int(input("1 file\n2 Alcatra\n3 Picanha: "))
kilos = 0
while(kilos == 0):
    kilos = float(input("Informe quantos kilos deseja"))
while(resposta.lower() != "sim" and resposta.lower() != "nao"):
    resposta = input("Cartao?")
print("Cupom fiscal")
print(nomedascarnes.get(tipo),"---",kilos)
if(kilos<5):
    valor = tabelaDePrecos.get(tipo).index(0) * kilos
    print("Valor:", valor)
else:
    valor = tabelaDePrecos.get(tipo).index(1) * kilos
    print("Valor:", valor)
if(resposta.lower() == "sim"):
    desconto = valor * 0.05
    print("Desconto:",  desconto)
else:
    desconto = 0
    print("Desconto:",  desconto)
print("Total a pagar:", valor - desconto)    
