# Ler as quatro notas e armazenar nas variáveis n1, n2, n3 e n4
n1, n2, n3, n4 = map(float, input().split())
# Realizar o cálcul oda média ponderada das notas com o seu peso
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10
# Exibir a média das notas
print(f"Media: {media:.1f}")
# Condição para avaliar se a nota é maior ou igual a 7.0
if media >= 7:
    # Exibir o resultado caso verdade
    print("Aluno aprovado.")
# Condição para avaliar se a nota é menor que 5.0
elif media < 5:
    # Exibir o resultado caso verdade
    print("Aluno reprovado.")
# Condição para avaliar se a nota é maior ou igual a 5.0 e menor que 7.0
else:
    # Exibir o resultado caso verdade
    print("Aluno em exame.")
    # Ler a nota de exame e armazenar na variável exame
    exame = float(input())
    # Exibir a nota de exame
    print(f"Nota do exame: {exame:.1f}")
    # Realizar o cálculo da nova média
    media_exame = (media + exame) / 2
    # Condição para avaliar se a nova média é maior ou igual a 5.0
    if media_exame >= 5:
        # Exibir o resultado caso verdade
        print("Aluno aprovado.")
    # Condição para avaliar se a nova média é menor que 5.0
    else:
        # Exibir o resultado caso verdade
        print("Aluno reprovado.")
    # Exibir o resultado
    print(f"Media final: {media_exame:.1f}")