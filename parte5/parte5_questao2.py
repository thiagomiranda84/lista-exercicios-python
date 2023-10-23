def is_primo(numero):
    if numero <= 1:
        return False  # Números menores ou iguais a 1 não são considerados primos

    for i in range(2, numero):
        if numero % i == 0:
            return False  # O número é divisível por outro número além de 1 e ele mesmo

    return True  # O número é primo

# Exemplos de uso da função
print(is_primo(7))  # Saída: True
print(is_primo(4))  # Saída: False