# Ler três valores e armazenar nas variáveis a, b e c
a, b, c = map(float, input().split())
# Criar uma lista com os três valores a, b e c
lista_valores = [a, b, c]
# Criar uma cópia dessa lista criada acima
lista_valores_copia = lista_valores.copy()
# Ordenar a primeira lista criada em ordem crescente
lista_valores.sort()
# Condição para avaliar se é um triângulo
if lista_valores[0] + lista_valores[1] > lista_valores[2]:
    # Realizar o cálculo do perimetro do triângulo
    perimetro = lista_valores[0] + lista_valores[1] + lista_valores[2]
    # Exbir o resultado
    print(f"Perimetro = {perimetro:.1f}")
else:
    # Realizar o cálculo da area do trapézio
    area = ((lista_valores_copia[0] + lista_valores_copia[1]) * lista_valores_copia[2]) / 2
    # Exbir o resultado
    print(f"Area = {area:.1f}")
