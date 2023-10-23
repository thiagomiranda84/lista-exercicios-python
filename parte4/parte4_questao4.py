# Crie uma lista desordenada com nomes de alunos
alunos = ["Ana", "Carlos", "Eduardo", "Beatriz", "Fernando", "Daniel", "Catarina", "Alice", "Bianca", "Gustavo"]

# Ordene a lista em ordem alfabética
alunos.sort()

# Exiba a lista ordenada
print("Lista ordenada de alunos:")
for aluno in alunos:
    print(aluno)

# Use o conceito de fatiamento para recuperar os nomes da 3ª a 7ª pessoa
terceira_a_setima = alunos[2:7]
print("\nNomes da 3ª à 7ª pessoa:")
for aluno in terceira_a_setima:
    print(aluno)

# Recupere e mostre os dois primeiros e os dois últimos nomes
dois_primeiros = alunos[:2]
dois_ultimos = alunos[-2:]
print("\nDois primeiros nomes:")
for aluno in dois_primeiros:
    print(aluno)
print("\nDois últimos nomes:")
for aluno in dois_ultimos:
    print(aluno)
