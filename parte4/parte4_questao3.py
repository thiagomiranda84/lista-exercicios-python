# Inicializa uma lista para armazenar as temperaturas em Fahrenheit
temperaturas = []

# Solicita ao usuário inserir as temperaturas em Fahrenheit
while True:
    temperatura_str = input("Insira uma temperatura em graus Fahrenheit (ou deixe em branco para encerrar): ")

    if temperatura_str == "":
        break

    temperaturas.append(float(temperatura_str))

# Converte as temperaturas de Fahrenheit para Celsius
temperaturas_celsius = []
for F in temperaturas:
    c= (F - 32) / 1.8
    temperaturas_celsius.append(c)

# Exibe as temperaturas em graus Fahrenheit e Celsius
print("Temperaturas:")
for i in range(len(temperaturas)):
    print(f"{temperaturas[i]:.2f}°F = {temperaturas_celsius[i]:.2f}°C")
