

nota1 = float( input("Digite a Nota 1 - Peso 2: ") )
nota2 = float( input("Digite a Nota 2 - Peso 3: ") )
nota3 = float( input("Digite a Nota 3 - Peso 5: ") )

# Calcula a média ponderada usando os pesos
peso_prova1 = 2
peso_prova2 = 3
peso_prova3 = 5

total_pesos = peso_prova1 + peso_prova2 + peso_prova3

media = ((nota1 * peso_prova1) + (nota2 * peso_prova2) + (nota3 * peso_prova3) ) / total_pesos

print(f"A média final do aluno é: {media:.2f}")
