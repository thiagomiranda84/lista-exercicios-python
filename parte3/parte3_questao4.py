# Solicita ao usuário um número inteiro N
N = int(input("Digite um número Inteiro: "))

# Inicializa a variável para a soma
soma = 0

# Utiliza um loop for para calcular a soma dos números de 1 a N
for i in range(1, N + 1):
    soma += i

# Exibe a soma dos números de 1 a N
print(f"Soma dos números de 1 a {N}: {soma}")
