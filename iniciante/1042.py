# Ler três números e armazenar nas variáveis n1, n2 e n3
n1, n2, n3 = map(int, input().split())
# Armazenar os valores na lista chamada original
original = [n1, n2, n3]
# Copiar a lista orginial para a lista numeros
numeros = original.copy()
# Ordenar os itens da lista em ordem crescente
numeros.sort()
# Laço for para apresentar os números em ordem crescente
for num in numeros:
    # Exibir o resultado
    print(num)
# Deixar uma linha em branco
print("")
# Laço for para apresentar os números na ordem que foi digitado pelo usuário
for num in original:
    # Exibir o resultado
    print(num)
