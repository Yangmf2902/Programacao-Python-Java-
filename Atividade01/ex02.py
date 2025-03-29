segundos = float(input("Digite um valor em segundos que será convertido em minutos, horas e dias: "))

min = segundos/60
hrs = min/60
dias = hrs/24

print(f"O tempo em segundos fornecido é equivalente a {min} minutos, {hrs} horas, e {dias} dias.")
