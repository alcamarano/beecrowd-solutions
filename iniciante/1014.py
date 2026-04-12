# Ler o valor da distânica percorrida em Km e armazenar na variável X
X = int(input("Informe a distância percorrida: "))
# Ler o valor total do combustível gasto e armazenar na variável Y
Y = float(input("Informe o combustível gasto: "))
# Realizar o cálculo do consumo médio do automóvel e armazenar na variável consumo
consumo = X/Y
# Exibir o resultado
print("{:.3f} km/l".format(consumo))