# Ler o número do funcionário e armazenar na variável numero_funcionario
numero_funcionario = int(input("Informe o número do funcionário: "))
# Ler as horas trabalhadas por este funcionário e armazenar na variável horas_trabalhadas
horas_trabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))
# Ler o valor da hora de trabalho do funcionário e armazenar na variável valor_hora
valor_hora = float(input("Informe o valor da hora de trabalho: U$ "))
# Exibir o número do funcionário
print("NUMBER =", numero_funcionario)
# Realizar o cálculo do salário deste funcionário
salario = valor_hora * horas_trabalhadas
# Exibir o salário do funcionário
print("SALARY = U$ {:.2f}".format(salario))