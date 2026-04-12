# Ler valor gasto em horas de uma viagem e armazenar na variável tempo_gasto
tempo_gasto = int(input("Informe o tempo gasto da viagem e horas: "))
# Ler a velocidade média durante esse tempo e armazenar na variável velocidade_media
velocidade_media = int(input("Informe a velociade média do automóvel na viagem: "))
# Realizar o cálculo do gasto de combustível para esta viagem e armazenar na variável litros
litros = (velocidade_media * tempo_gasto) / 12
# Exibir o resultado
print(f"{litros:.3f}")