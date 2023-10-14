def elementosRepetidos(lista):
  keys = {}
  repetidos = {}
  for ele in lista:
    if(ele in keys):
      repetidos[ele] = 1
    keys[ele] = [ele]
  print(repetidos.keys())

while(True):
  i = []
  numero = 1
  while(numero != 0):
    numero = int(input("Digite o numero da lista"))
    if(numero == 0):
      break
    i.append(numero)
  elementosRepetidos(i[0:len(i)])