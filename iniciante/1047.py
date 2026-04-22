# Lê os quatro números da entrada e já converte para inteiro
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())
# Converte tudo para minutos
inicio_total = hora_inicial * 60 + minuto_inicial
fim_total = hora_final * 60 + minuto_final
# Inicializa as variáveis
horas = 0
minutos = 0
# Caso 1: início e fim iguais → duração máxima de 24h
if inicio_total == fim_total:
    horas = 24
# Caso 2: início maior que fim → jogo passou da meia-noite
# Soma o tempo até a meia-noite (1440 - inicio) com o tempo após ela (fim)
elif inicio_total > fim_total:
    duracao = ((1440 - inicio_total) + fim_total)
    horas = duracao // 60
    minutos = duracao % 60
# Caso 3: início menor que fim → jogo dentro do mesmo dia
# Basta subtrair o início do fim
elif inicio_total < fim_total:
    horas = (fim_total - inicio_total) // 60
    minutos = (fim_total - inicio_total) % 60
# Exibir o resultado
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
