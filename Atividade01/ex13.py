salario = float(input("Digite seu salário: "))
percentual = float(input("Digite o percentual de aumento no primeiro ano: "))
anos = int(input("Digite por quantos anos você trabalhou: "))
novo_salario = salario+(salario*(percentual)/100)
for x in range(anos+1):
	novo_salario = novo_salario+(novo_salario*(percentual*2)/100)
print(f"O salário final foi igual a: {novo_salario} reais.")
