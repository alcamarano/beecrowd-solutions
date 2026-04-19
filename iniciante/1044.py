# Ler dois valores e armazenar nas variáveis A e B
a, b = map(int, input().split())
# Condição para avaliar se são multiplos ou não
if a % b == 0 or b % a == 0:
    # Exibir resultado caso verdade
    print("Sao Multiplos")
elif a == 0 or b == 0:
    # Exibir resultado caso verdade
    print("Nao sao Multiplos")
else:
    # Exibir resultado caso verdade
    print("Nao sao Multiplos")
