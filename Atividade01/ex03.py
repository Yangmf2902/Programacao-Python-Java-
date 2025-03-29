valor = float(input("Digite o valor total das mercadorias: "))

if valor > 500:
	taxa = (valor-500)+(valor-500)/2
	valor_total = valor+taxa
else:
	valor_total = valor
print("O valor final das compras foi de {valor_total} reais.")
