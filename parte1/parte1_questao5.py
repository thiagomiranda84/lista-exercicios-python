# Solicita o valor em real e a cotação do dólar ao usuário
valor_em_real = float(input("Digite o valor em real: R$"))
cotacao_dolar = float(input("Digite a cotação do dólar em reais (exemplo: 5.50): "))

# Calcula o valor em dólar correspondente
valor_em_dolar = valor_em_real / cotacao_dolar

# Exibe o valor em dólar
print(f"O valor em dólar é: ${valor_em_dolar:.2f}")