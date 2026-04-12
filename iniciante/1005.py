# Ler duas notas e armazenar nas variáveis A e B
A = float(input("Informe a primeira nota: "))
B = float(input("Informe a segunda nota: "))
# Realizar o cálculo da méda ponderada das notas com o seu peso
MEDIA = (A * 3.5 + B * 7.5) / 11
# Exibir o resultado
print("MEDIA = {:.5f}".format(MEDIA))