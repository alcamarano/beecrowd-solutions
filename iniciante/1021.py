n = round(float(input()) * 100)
cedulas = [10000, 5000, 2000, 1000, 500, 200]
moedas  = [100, 50, 25, 10, 5, 1]
nomes_c = [100, 50, 20, 10, 5, 2]
nomes_m = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
resto = n
print("NOTAS:")
for valor, nome in zip(cedulas, nomes_c):
    qtd = resto // valor
    resto %= valor
    print(f"{qtd} nota(s) de R$ {nome:.2f}")
print("MOEDAS:")
for valor, nome in zip(moedas, nomes_m):
    qtd = resto // valor
    resto %= valor
    print(f"{qtd} moeda(s) de R$ {nome:.2f}")