import math

def temRaizInteira(numero):
  return math.sqrt(numero)

def ehPrimo(numero):
  raizInteiraMaisProxima = int(temRaizInteira(numero))
  for i in range (2,raizInteiraMaisProxima + 1):
    if(numero % i == 0):
      return False
    i+=1    
  return True


def menu():
  numero = int(input("Informe o numero que deseja saber se é primo: "))
  print(ehPrimo(numero))

while(True):
  menu()