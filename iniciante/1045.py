# Ler três valores referente a cada lado e armazenar nas variáveis A, B e C
a, b, c = map(float, input().split())
# O maior lado deve ser A para que as comparações seguintes sejam válidas
a, b, c = sorted([a, b, c], reverse=True)
# Condição de existência: o maior lado deve ser menor que a soma dos outros dois
if a >= b + c:
    # Exibir resultado caso verdade
    print("NAO FORMA TRIANGULO")
else:
    # Armazenar nas variáveis a2, b2 e c2 o quadrado das variáveis A, B e C
    a2, b2, c2 = a**2, b**2, c**2
    # Teorema de Pitágoras generalizado: A² vs B²+C² determina o tipo de ângulo
    if a2 == b2 + c2:
        # Exibir resultado caso verdade
        print("TRIANGULO RETANGULO")
    elif a2 > b2 + c2:
        # Exibir resultado caso verdade
        print("TRIANGULO OBTUSANGULO")
    else:
        # Exibir resultado caso verdade
        print("TRIANGULO ACUTANGULO")
    # Verificação independente: um triângulo pode ser isósceles e obtusângulo, por exemplo
    if a == b == c:
        # Exibir resultado caso verdade
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        # Exibir resultado caso verdade
        print("TRIANGULO ISOSCELES")
