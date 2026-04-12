# Ler o nome do vendedor
nome = input("Informe o nome do vendedor: ")
# Ler o valor do salário fixo do vendedor e armazenar na variável salario_fixo
salario_fixo = float(input("Informe o salario fixo do vendedor: R$ "))
# Ler o valor da comissão deste vendedor e armazenar na variável comissão
comissao = float(input("Informe o comissao do vendedor: "))
# Realizar o cálculo do salário final deste vendedor
salario_final = salario_fixo + (comissao * 0.15)
# Exibir o resultado
print("TOTAL = R$ {:.2f}".format(salario_final))