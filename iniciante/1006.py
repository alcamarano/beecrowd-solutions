# Ler três notas e armazenar nas variáveis A, B e C
A = float(input("Informe a primeira nota: "))
B = float(input("Informe a segunda nota: "))
C = float(input("Informe a terceira nota: "))
# Realizar o cálculo da méda ponderada das notas com o seu peso
MEDIA = (A * 2 + B * 3 + C * 5) / 10
# Exibir o resultado
print("MEDIA = {:.1f}".format(MEDIA))