# Solicita ao usuário um número inteiro menor que 1000
numero = int(input("Digite um número inteiro menor que 1000: "))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = (numero % 100) % 10

if centenas > 0:
    print(f"{centenas} centena(s)")
if dezenas > 0:
    print(f"{dezenas} dezena(s)")
if unidades > 0:
    print(f"{unidades} unidade(s)")