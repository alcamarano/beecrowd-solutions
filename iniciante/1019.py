# Ler o valor em segundos de um evento e armazenar na variável segundos
segundos = int(input("Informe a quantidade de segundos de um evento: "))
# Realizar o cálculo transformando em hh:mm:ss
horas = segundos // 3600
minutos = segundos // 60 % 60
segundos %= 60
# Exibir o resultado
print(f"{horas}:{minutos}:{segundos}")