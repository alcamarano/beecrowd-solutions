# Importar da biblioteca math o sqrt
from math import sqrt
# Ler os três valores e armazenar nas variáveis A, B e C
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
# Condição para analisar se A é igual a zero
if A == 0:
    # Exibir resultado caso verdade
    print("Impossivel calcular")
else:
    # Realizar o cálculo de delta
    delta = B ** 2 - 4 * A * C
    # Condição para analisar se delta é menor que zero
    if delta < 0:
        # Exibir resultado caso verdade
        print("Impossivel calcular")
    else:
        # Reazliar o cálculo de X1 e X2 e armazenar nas variáveis X1 e X2
        x1 = (-B + sqrt(delta)) / (2 * A)
        x2 = (-B - sqrt(delta)) / (2 * A)
        # Exibir o resultado
        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")