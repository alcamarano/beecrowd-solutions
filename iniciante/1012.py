# Ler três valores e armazenar nas variáveis A, B e C
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
# Realizar o cálculo da área do triângulo retângulo que tem A por base e C por altura
triangulo = (A * C) / 2
# Realizar o cálculo da área do círculo de raio C
circulo = 3.14159 * C ** 2
# Realizar o cálculo área do trapézio que tem A e B por bases e C por altura
trapezio = ((A + B) * C) / 2
# Realizar o cálculo da área do quadrado que tem lado B
quadrado = B ** 2
# Realizar o cálculo da área do retângulo que tem lados A e B
retangulo = A * B
# Exibir os resultados
print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))