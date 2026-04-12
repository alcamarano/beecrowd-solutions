# Ler um valor em reais, converter para centavos e armazenar na variável n
n = round(float(input()) * 100)
# Tuplas com os valores em centavos e os nomes das cédulas e moedas
cedulas = (10000, 5000, 2000, 1000, 500, 200)
moedas  = (100, 50, 25, 10, 5, 1)
nomes_c = (100, 50, 20, 10, 5, 2)
nomes_m = (1.00, 0.50, 0.25, 0.10, 0.05, 0.01)
# Variável para controlar o resto da decomposição
resto = n
# Exibir o cabeçalho das notas
print("NOTAS:")
# Laço for para percorrer as cédulas e decompor o valor em notas
for valor, nome in zip(cedulas, nomes_c):
    # Calcular a quantidade de notas da cédula atual
    qtd = resto // valor
    # Atualizar o resto após retirar as notas da cédula atual
    resto %= valor
    # Exibir a quantidade e o nome da cédula atual
    print(f"{qtd} nota(s) de R$ {nome:.2f}")
# Exibir o cabeçalho das moedas
print("MOEDAS:")
# Laço for para percorrer as moedas e decompor o restante
for valor, nome in zip(moedas, nomes_m):
    # Calcular a quantidade de moedas do valor atual
    qtd = resto // valor
    # Atualizar o resto após retirar as moedas do valor atual
    resto %= valor
    # Exibir a quantidade e o valor da moeda atual
    print(f"{qtd} moeda(s) de R$ {nome:.2f}")