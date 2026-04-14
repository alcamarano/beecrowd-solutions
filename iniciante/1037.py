# Ler um número com casas decimais e armazenar na variável num
num = float(input("Informe um número para saber se está ou não dentro do intervalo: "))
# Condição para avaliar se está dentro de [0,25]
if 0 <= num <= 25:
    # Exibir resultado caso verdade
    print("Intervalo [0,25]")
# Condição para avaliar se está dentro de (25,50]
elif 25 < num <= 50:
    # Exibir resultado caso verdade
    print("Intervalo (25,50]")
# Condição para avaliar se está dentro de (50,75]
elif 50 < num <= 75:
    # Exibir resultado caso verdade
    print("Intervalo (50,75]")
# Condição para avaliar se está dentro de (75,100]
elif 75 < num <= 100:
    # Exibir resultado caso verdade
    print("Intervalo (75,100]")
# Condição para avaliar se está fora do intervalo
else:
    # Exibir resultado caso verdade
    print("Fora de intervalo")