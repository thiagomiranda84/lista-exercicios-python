def calcular_cedulas(valor):
    print(f"Valor informado: R$ {valor}")

    cedulas = [100, 50, 20, 10, 5, 2, 1]  # Valores das cédulas disponíveis
    quantidades = [0, 0, 0, 0, 0, 0, 0]  # Inicializa o contador de quantidades de cédulas

    for i in range(len(cedulas)):
        while valor >= cedulas[i]:
            valor -= cedulas[i]
            quantidades[i] += 1

    for i in range(len(cedulas)):
        print(f"{quantidades[i]} nota(s) de R${cedulas[i]}")


# Exemplo de uso da função
valor = 254
calcular_cedulas(valor)