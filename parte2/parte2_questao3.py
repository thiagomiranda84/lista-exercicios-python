# Solicita ao usuário o peso (em quilogramas) e a altura (em metros)
peso = float(input("Informe o peso (em quilogramas): "))
altura = float(input("Informe a altura (em metros): "))

# Calcula o IMC (Índice de Massa Corporal)
imc = peso / (altura ** 2)

# Determina a faixa de peso com base no IMC

if imc < 18.5:
    faixa_peso = "Abaixo do peso"
elif 18.5 <= imc < 25:
    faixa_peso = "Peso normal"
elif 25 <= imc < 30:
    faixa_peso = "Sobrepeso"
elif 30 <= imc < 35:
    faixa_peso = "Obesidade grau 1"
elif 35 <= imc < 40:
    faixa_peso = "Obesidade grau 2"
else:
    faixa_peso = "Obesidade grau 3"

# Exibe o IMC e a faixa de peso correspondente
print(f"Seu IMC é: {imc:.2f}")
print(f"Faixa de peso: {faixa_peso}")