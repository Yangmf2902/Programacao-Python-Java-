n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))

media = (n1+ n2 +n3)/3
ponderada1 = ((n1*2)+(n2*2)+(n3*3))/7
ponderada2 = ((n1*1)+(n2*2)+(n3*2))/5

print(f"Sua média aritmética é igual a: {media}.")
print(f"Sua média com os respectivos pesos 2, 2 e 3 é igual a: {ponderada1}.")
print(f"Sua média com os respectivos pesos 1, 2 e 2 é igual a: {ponderada1}.")
