# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa o resultado com 1
resultado = 1

# Calcula o fatorial usando um loop for decrescente
if numero == 0:
    print(f"O fatorial de 0 é {resultado}.")
else:
    for i in range(numero, 0, -1):
        resultado *= i

    print(f"O fatorial de {numero} é: {resultado}")