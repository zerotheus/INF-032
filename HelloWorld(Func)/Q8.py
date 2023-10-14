def ehPrefixo(pre, palavra):
  contaigual = 0
  print(len(pre))
  for i in range (0, len(palavra)):
    print(i)
    print(contaigual)
    if(contaigual == len(pre)):
      return True
    if(i<len(pre)):
      if(pre[i].lower() == palavra[i].lower()):
        contaigual+=1
        i+=1
      else:
        return False
    


while(True):
  print(ehPrefixo(input("Digite a palavra pre"), input("Digite a palavra base")))