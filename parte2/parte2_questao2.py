
# Solicita ao usuário as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média do aluno
media = (nota1 + nota2) / 2

# Atribui um conceito com base na média
if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

# Exibe a média e o conceito
print(f"Média do aluno: {media:.2f}")
print(f"Conceito: {conceito}")