# Duas listas para comparação
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

# Converta as listas em conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Valores comuns às duas listas
comuns = conjunto1.intersection(conjunto2)
print("Valores comuns às duas listas:", comuns)

# Valores que só existem na primeira lista
so_na_lista1 = conjunto1.difference(conjunto2)
print("Valores que só existem na primeira lista:", so_na_lista1)

# Valores que existem apenas na segunda lista
so_na_lista2 = conjunto2.difference(conjunto1)
print("Valores que existem apenas na segunda lista:", so_na_lista2)

# Lista com elementos não repetidos das duas listas
nao_repetidos = conjunto1.union(conjunto2)
print("Lista com elementos não repetidos das duas listas:", nao_repetidos)

# Primeira lista sem os elementos repetidos na segunda
lista1_sem_repetidos_lista2 = conjunto1.difference(conjunto2)
print("Primeira sem os elementos repetidos na segunda:", lista1_sem_repetidos_lista2)
