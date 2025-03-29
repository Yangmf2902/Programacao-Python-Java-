dias = int(input("Digite quantos dias você rodou com o carro: "))
km = int(input("Digite quantos km você rodou com o carro: "))

taxa = 0

if km > 100:
	taxa = (km-100)*12

valor_total = (90*dias) + taxa

print("O valor total a ser pago será de {valor_total} reais.")
