n = int(input("Digite um número inteiro maior que 1: "))
while n <= 1:
	n = int(input("Digite um número inteiro maior que 1: "))
divisores = []
for x in range(1, n+1):
	if n % x == 0:
		divisores.append(x)
if len(divisores) > 2:
	print("O número digitado não é primo.")
elif len(divisores) == 2:
	print("O número digitado é primo.")
