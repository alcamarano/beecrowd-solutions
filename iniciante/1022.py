# Ler quatro valores e armazenar nas variáveis A, B, C e D
A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
# Condição
if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    # Exibir o resultado caso verdade
    print("Valores aceitos")
else:
    # Exibir o resultado caso falso
    print("Valores nao aceitos")