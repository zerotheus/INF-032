agenda = {}
telefones = 0
operacao = ""
limite = 10
print(agenda)
while(operacao != "0"):
    operacao = input("0 sair\n1 Adicionar Nome na Agenda\n2 Adicionar Telefone\n3 Excluir Telefone\n4 Excluir nome \n5 Consultar Telefone\n")
    if(operacao == "1"):
      if(telefones == 10):
         print("limite de telefones atingido")
         continue
      nome = input("Digite o nome da Pessoa ")
      if(nome in agenda):
         print("O nome deve ser novo")
         continue
      numero = [input("Informe o numero da Pessoa " + nome + " ")]
      agenda[nome] = numero
      telefones = telefones + 1
    if(operacao == "2"):
      if(telefones == 10):
         print("limite de telefones atingido")
         continue
      nome = input("Digite o nome da Pessoa ")
      if(nome not in agenda):
         if(input("Pessoa nao Encontrada\nDigite sim para incluir ").lower() == "sim"):
            numero = [input("Informe o numero da Pessoa ")]
            agenda[nome] = numero
            telefones = telefones + 1
            continue
         else:
            operacao = 0
            continue
      numeros = agenda.get(nome)
      numero.append(input("Informe o numero da Pessoa " + nome + " "))
      telefones = telefones + 1
    if(operacao == "3"):
      nome = input("Informe o nome da pessoa que deseja excluir um telefone ")
      if(nome in agenda):
        numeros = agenda.get(nome)
        if(len(numeros) > 1):
           numeros.pop()
           telefones = telefones - 1
        else:
           agenda.pop(nome)
           telefones = telefones - 1
      else:
           print("Pessoa nao encontrada")
    if(operacao == "4"):
      nome = input("Informe o nome da pessoa que deseja excluir um telefone ")
      if(nome in agenda):
         telefones = telefones - len(agenda.get(nome)) 
         agenda.pop(nome)
      else:
           print("Pessoa nao encontrada")
    if(operacao == "5"):
        nome = input("Informe o nome da pessoa que seja consultar ")
        if(nome in agenda):
          print(agenda.get(nome))
        else:
           print("Pessoa nao encontrada")
    if(operacao == "0"):
       break
    print(agenda)
    print("tel",telefones)  
print(agenda)