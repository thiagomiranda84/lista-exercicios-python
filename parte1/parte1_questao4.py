# Solicita o valor do celular e o número de parcelas ao usuário
valor_celular = float(input("Digite o valor do celular: R$"))
parcelas = int(input("Digite o número de parcelas (0 a 12): "))

# Define a taxa de juros mensal (2% ou 0,02)
taxa_juros_mensal = 0.02

# Calcula o valor total com juros
montante = valor_celular * (1 + taxa_juros_mensal) ** parcelas

# Exibe o valor total a ser pago por Maria
print(f"O valor total a ser pago por Maria será de R${montante:.2f} em {parcelas} parcelas de R${montante / parcelas:.2f} cada.")