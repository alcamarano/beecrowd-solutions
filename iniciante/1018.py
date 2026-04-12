# Ler um valor em reais para decompor em notas e armazenar na variável n
n = int(input("Informe um valor em reais sem os centavos: R$ "))
# Tupla com as cédulas
cedulas = (100, 50, 20, 10, 5, 2, 1)
# Variável para controlar o resto
resto = n
# Exibir o valor informado na variável n
print(n)
# Laço for para percorrer as cédulas e decompor o valor em notas
for valor in cedulas:
    # Calcular a quantidade de notas da cédula atual
    qtd = resto // valor
    # Atualizar o resto após retirar as notas da cédula atual
    resto %= valor
    # Exibir o resultado
    print(f"{qtd} nota(s) de R$ {valor},00")