nome = input("Digite seu nome")

nota1 = int(input("Nota 1"))
nota2 = int(input("Nota 2"))

media =( nota1 + nota2)/2

if(media >= 7):
    print("aprovado")
if(media < 3):
    print("reprovado")
if(media >3 and media < 7):
    print("Prova final")    
    
