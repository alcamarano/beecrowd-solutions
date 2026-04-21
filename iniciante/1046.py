# Ler a hora inicial e hora final e armazenar nas variáveis hora_inicial e hora_final
hora_inicial, hora_final = map(int, input().split())
# Iniciar a variável duração zerada
duracao = 0
# Condição para avaliar se o jogo ocorreu no mesmo dia
if hora_final > hora_inicial:
    duracao = hora_final - hora_inicial
# Condição para avaliar se o jogo começou em um dia e termino no dia seguinte
elif hora_final < hora_inicial:
    duracao = 24 - hora_inicial + hora_final
# Condição para avaliar se hora inicial é igual a final
elif hora_inicial == hora_final:
    duracao = 24
# Exibir o resultado
print(f"O JOGO DUROU {duracao} HORA(S)")
