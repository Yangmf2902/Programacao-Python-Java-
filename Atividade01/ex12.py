n_salas = int(input("Digite a quantidade de salas: "))
alunos_total = 0

for x in range(turmas):
    alunos_sala = int(input(f"Digite a quantidade de alunos na turma {x + 1}: "))
    alunos_total += alunos_sala
    if alunos > 40:
        print(f"A turma {x + 1} tem mais de 40 alunos.")

media = alunos_total / n_salas
print(f"A média de alunos por sala é {media}."")
