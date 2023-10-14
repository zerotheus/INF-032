def menu():
	entrada = input("Deseja converter a tempearatura para Celsius ou Farenheit: ")
	if(entrada[0].lower() == "c"):
		print(converteParaCelcius())
	if(entrada[0].lower() == "f"):
		print(converteParaFarenheit())

def converteParaCelcius():
	far =float(input("Informe a temperatura"))
	return (far - 32) * 5/9
def converteParaFarenheit():
	cel =float(input("Informe a temperatura"))
	return (cel * 9/5) + 32


while(True):
	menu()