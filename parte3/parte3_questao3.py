# Solicita ao usuário o início e o fim do intervalo
inicio = int(input("Início do intervalo: "))
fim = int(input("Fim do intervalo: "))

# Inicializa a contagem de números pares
numeros_pares = 0

# Utiliza um loop for para calcular a quantidade de números pares
for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        numeros_pares += 1

# Exibe a quantidade de números pares no intervalo
print(f"Quantidade de números pares: {numeros_pares}")