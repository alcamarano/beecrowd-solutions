# Ler a idade de uma pessoa em dias e armazenar na variável idade_dias
idade_dias = int(input("Informe a idade de uma pessoa em dias: "))
# Tuplas para armazenar nomes e o tempo
nomes = ("ano(s)", "mes(es)", "dia(s)")
tempo = (365, 30, 1)
# Variável para controlar o resto da decomposição
resto = idade_dias
# Laço for para percorrer as unidades de tempo e decompor a idade
for valor, nome in zip(tempo, nomes):
    # Calcular a quantidade da unidade de tempo atual
    unidade = resto // valor
    # Atualizar o resto após retirar a unidade de tempo atual
    resto %= valor
    # Exibir o resultado
    print(f"{unidade} {nome}")