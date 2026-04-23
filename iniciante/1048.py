# Lê o salário atual informado pelo usuário
salario_atual = float(input())
# Inicializa as variáveis de reajuste e percentual com zero
reajuste = 0
percentual = 0
# Determinar o percentual de reajuste com base na faixa salarial
match salario_atual:
    case _ if salario_atual <= 400:
        percentual = 15
        reajuste = salario_atual * (percentual / 100)
    case _ if salario_atual <= 800:
        percentual = 12
        reajuste = salario_atual * (percentual / 100)
    case _ if salario_atual <= 1200:
        percentual = 10
        reajuste = salario_atual * (percentual / 100)
    case _ if salario_atual <= 2000:
        percentual = 7
        reajuste = salario_atual * (percentual / 100)
    case _ if salario_atual > 2000:
        percentual = 4
        reajuste = salario_atual * (percentual / 100)
# Calcular o novo salário somando o valor do reajuste ao salário atual
novo_salario = salario_atual + reajuste
# Exibir o resultado
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
