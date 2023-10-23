# Solicita ao usuário o valor da dívida, a taxa de juros mensal e o valor mensal a ser pago
divida = float(input("Valor da dívida: R$"))
taxa_juros_mensal = float(input("Taxa de juros mensal (%): ")) / 100
pagamento_mensal = float(input("Valor mensal a ser pago: R$"))

# Inicializa o contador de meses
meses = 0

# Calcula o tempo necessário para quitar a dívida
while divida > 0:
    divida = divida + (divida * taxa_juros_mensal)
    divida = divida - pagamento_mensal
    meses += 1

# Exibe o resultado
print(f"Serão necessários {meses} meses para quitar a dívida.")