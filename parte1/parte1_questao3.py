# Solicita a distância a ser percorrida e o consumo médio de combustível ao usuário
distancia = float(input("Digite a distância a ser percorrida (em quilômetros): "))
consumo_medio = float(input("Digite o consumo médio de combustível (em quilômetros por litro): "))

# Calcula a quantidade de combustível necessária
quantidade_combustivel = distancia / consumo_medio

# Exibe a quantidade de combustível necessária
print(f"Para percorrer {distancia} quilômetros, você precisará de {quantidade_combustivel:.2f} litros de combustível.")
