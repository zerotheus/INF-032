
def ehPerfeito(numero):
  soma = 0
  for i in range(1, numero//2 + 1):
    if(numero % i ==0):
      soma+=i
  if(soma == numero or numero == 1):
    return True
  return False


def menu():
  numero=int(input("Digite o inteiro q deseja saber se é perfeito"))
  print(ehPerfeito(numero))

while(True):
  menu()