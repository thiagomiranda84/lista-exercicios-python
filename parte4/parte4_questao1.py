lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# a) Imprime o maior elemento
maior_elemento = max(lista)
print(f"a) Maior elemento: {maior_elemento}")

# b) Imprime o menor elemento
menor_elemento = min(lista)
print(f"b) Menor elemento: {menor_elemento}")

# c) Imprime os números pares
numeros_pares = [num for num in lista if num % 2 == 0]
print(f"c) Números pares: {numeros_pares}")

# d) Imprime o número de ocorrências do primeiro elemento da lista
primeiro_elemento = lista[0]
ocorrencias_primeiro_elemento = lista.count(primeiro_elemento)
print(f"d) Ocorrências do primeiro elemento: {ocorrencias_primeiro_elemento}")

# e) Imprime a média dos elementos
media = sum(lista) / len(lista)
print(f"e) Média dos elementos: {media:.2f}")

# f) Imprime a soma dos elementos de valor negativo
soma_negativos = sum(num for num in lista if num < 0)
print(f"f) Soma dos elementos negativos: {soma_negativos}")

# g) Imprime a lista ordenada
lista_ordenada = sorted(lista)
print(f"g) Lista ordenada: {lista_ordenada}")
