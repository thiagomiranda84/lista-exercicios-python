# Solicita ao usuário o tipo de combustível e o número de litros vendidos
tipo_combustivel = input("Informe o tipo de combustível (A-álcool, G-gasolina): ")
litros_vendidos = int(input("Informe o número de litros vendidos: "))

# Preços por litro
preco_gasolina = 6.20
preco_alcool = 4.90

# Inicializa o desconto
desconto = 0

# Calcula o valor a ser pago
if tipo_combustivel == "A":
    if litros_vendidos <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor_a_pagar = litros_vendidos * (preco_alcool - (preco_alcool * desconto))
elif tipo_combustivel == "G":
    if litros_vendidos <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor_a_pagar = litros_vendidos * (preco_gasolina - (preco_gasolina * desconto))
else:
    print("Tipo de combustível inválido. Use 'A' para álcool ou 'G' para gasolina.")
    valor_a_pagar = 0

# Exibe o valor a ser pago pelo cliente
print(f"Valor a Pagar: {valor_a_pagar:.2f}")
