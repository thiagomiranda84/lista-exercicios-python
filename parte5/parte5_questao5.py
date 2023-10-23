# Inicializa a variável global "total"
total = 0

# Função para calcular o total das vendas
def calcular_total(valor, quantidade):
    global total  # Indica que estamos usando a variável global "total"
    total += valor * quantidade

# Chame a função para registrar as vendas
calcular_total(10, 2)  # Venda de um item de R$10, quantidade: 5
calcular_total(15, 3)   # Venda de um item de R$5, quantidade: 3
calcular_total(5, 5)   # Venda de um item de R$8, quantidade: 2

# Apresente o total das vendas realizadas
print(f"Total das vendas realizadas: R${total:.2f}")
