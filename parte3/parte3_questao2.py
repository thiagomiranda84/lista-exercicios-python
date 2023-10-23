# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Inicializa o contador
contador = 1

# Exibe a tabuada de multiplicação
print(f"Tabuada do número {numero}:")

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1