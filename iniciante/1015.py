# Importar da biblioteca math o sqrt
from math import sqrt
# Ler dois pontos x e y, e armazenar nas variáveis x1 e y1
x1, y1 = input().split()
# Ler dois pontos x e y, e armazenar nas variáveis x2 e y2
x2, y2 = input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
# Realizar o cálculo da distância entre os dois pontos
distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)
# Exibir o resultado
print(f"{distancia:.4f}")