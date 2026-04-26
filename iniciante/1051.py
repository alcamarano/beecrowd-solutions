# Lê o salário com casas decimais
salario = float(input())
# Inicializa o imposto zerado para acumular as faixas
imposto = 0
# Faixa de 8%: tributa apenas o trecho entre R$ 2000 e R$ 3000
if salario > 2000:
    imposto += (min(salario, 3000) - 2000) * 0.08
# Faixa de 18%: tributa apenas o trecho entre R$ 3000 e R$ 4500
if salario > 3000:
    imposto += (min(salario, 4500) - 3000) * 0.18
# Faixa de 28%: tributa tudo que ultrapassar R$ 4500 (sem teto)
if salario > 4500:
    imposto += (salario - 4500) * 0.28
# Exibe o resultado: isento para salários até R$ 2000, ou o imposto calculado
if salario <= 2000:
    print("Isento")
else:
    print(f"R$ {imposto:.2f}")
