# Ler três valores e armazenar nas variáveis A, B e C
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
# Realizar o cálculo para identificar se A ou B é maior e armazenar na variável MaiorAB
MaiorAB = (a+b+abs(a-b))/2
# Condição para verificar de MaiorAB é maior que C ou não
if (MaiorAB > c):
    # Exibir o resultado caso verdade
    print("{:.0f} eh o maior".format(MaiorAB))
else:
    # Exibir o resultado caso falso
    print("{:.0f} eh o maior".format(c))