def contaLetra(palavra,letra):
  conta = 0
  for l in palavra:
    if(l == palavra.lower()):
      conta += 1
  return conta
while(True):
  print(contaLetra(input("Digite a letra"),input("Digite a palavra")))