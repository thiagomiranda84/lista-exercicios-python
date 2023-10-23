def sublista_limite(lista, limite_inferior, limite_superior):
    sublista = []
    for numero in lista:
        if limite_inferior <= numero <= limite_superior:
            sublista.append(numero)
        elif numero > limite_superior:
            break  # Os elementos seguintes são maiores do que o limite superior, podemos encerrar a busca
    return sublista

# Exemplo de uso da função
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
limite_inf = 3
limite_sup = 7

resultado = sublista_limite(numeros, limite_inf, limite_sup)
print(resultado)  # Saída: [3, 4, 5, 6, 7]