print("informe a valor hora aula")
valorHoraAula = int(input())
print("informe a quantidade de horas")
HorasDeAulas = int(input())
print("informe percentual de desconto do inss (SEM %)")
porcentualDeInss = 1-int(input())/100
salarioliquido = valorHoraAula*HorasDeAulas*porcentualDeInss
print(salarioliquido)
