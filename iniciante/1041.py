# Ler as duas coordenadas e armazenar nas variáveis x e y
x, y = map(float, input().split())
# Condições para avaliar o quadrante das coordenadas
if x == 0 and y == 0:
    # Exibir resultado caso verdade
    print("Origem")
elif x == 0:
    # Exibir resultado caso verdade
    print("Eixo Y")
elif y == 0:
    # Exibir resultado caso verdade
    print("Eixo X")
elif x > 0 and y > 0:
    # Exibir resultado caso verdade
    print("Q1")
elif x < 0 and y > 0:
    # Exibir resultado caso verdade
    print("Q2")
elif x < 0 and y < 0:
    # Exibir resultado caso verdade
    print("Q3")
else:
    # Exibir resultado caso verdade
    print("Q4")
