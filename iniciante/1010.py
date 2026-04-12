# Ler código, qunatidade e valor de uma peça e armazenar nas variáveis cod1, quant1 e valor1
cod1, quant1, valor1 = input().split()
cod1 = int(cod1)
quant1 = int(quant1)
valor1 = float(valor1)
# Ler código, qunatidade e valor de outra peça e armazenar nas variáveis cod2, quant2 e valor2
cod2, quant2, valor2 = input().split()
cod2 = int(cod2)
quant2 = int(quant2)
valor2 = float(valor2)
# Realizar o cálculo do valor total das peças
total = (quant1 * valor1) + (quant2 * valor2)
# Exibir o resultado
print("VALOR A PAGAR: R$ {:.2f}".format(total))