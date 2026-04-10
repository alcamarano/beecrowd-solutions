idade_dias = int(input())
nomes = ["ano(s)", "mes(es)", "dia(s)"]
tempo = [365, 30, 1]
resto = idade_dias
for valor, nome in zip(tempo, nomes):
    unidade = resto // valor
    resto %= valor
    print(f"{unidade} {nome}")