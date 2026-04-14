# Ler o código e a quantidade e armazenar nas variáveis cod e quant
cod, quant = input().split()
cod = int(cod)
quant = int(quant)
# Variável preco criada e definida como zero
preco = 0
# Calcular o preço total conforme o produto selecionado pelo código
match cod:
    case 1:
        # Calcular caso produto código 1
        preco = 4.00 * quant
    case 2:
        # Calcular caso produto código 2
        preco = 4.50 * quant
    case 3:
        # Calcular caso produto código 3
        preco = 5.00 * quant
    case 4:
        # Calcular caso produto código 4
        preco = 2.00 * quant
    case 5:
        # Calcular caso produto código 5
        preco = 1.50 * quant
# Exibir o resultado
print(f"Total: R$ {preco:.2f}")