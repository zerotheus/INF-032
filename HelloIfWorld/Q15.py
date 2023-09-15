salario = float(input("Digite o salario"))
prestacao = float(input("informe a prestacao"))

if(prestacao/salario > 0.3 and prestacao/salario > 0):
    print("nao tem emprestimo")
else:
    print("tem emprestimo")