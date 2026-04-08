n = int(input())
cedulas = [100, 50, 20, 10, 5, 2, 1]
resto = n
print(n)
for valor in cedulas:
    qtd = resto // valor
    resto %= valor
    print(f"{qtd} nota(s) de R$ {valor},00")