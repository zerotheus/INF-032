print("Digite o Dividendo")
dividendo = int(input())
print("Digite o divisor")
divisor =int(input())
quociente = dividendo//divisor
resto = dividendo % divisor
output = "Dividendo {} divisor {} quociente {} resto {}"
print(output.format(dividendo,divisor,quociente,resto))