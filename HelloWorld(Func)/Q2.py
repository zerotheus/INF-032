def entrada():
  numero = int(input("Informe um numero inteiro positivo"))
  vetor = [1,1]
  if(numero > 2):
    print(fibo(numero - 1, vetor[0:2]))
  elif(numero <= 2):
    print(1)

def fibo(numero, vetor):
  fib = []
  fib = vetor
  aux = fib[1]
  fib[1] = fib[0] + fib[1]
  fib[0] = aux
  if(numero == 2):
    return fib[1]
  return fibo(numero - 1, fib[0:2])


while(True):
  entrada()
