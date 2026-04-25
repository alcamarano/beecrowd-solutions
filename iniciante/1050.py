# Dicionário que mapeia DDDs para suas respectivas cidades
ddd = {
    61: "Brasilia", 71: "Salvador", 11: "Sao Paulo", 21: "Rio de Janeiro", 32: "Juiz de Fora",
    19: "Campinas", 27: "Vitoria", 31: "Belo Horizonte"
}
# Lê o DDD digitado pelo usuário
ddd_usuario = int(input())
# Verifica se o DDD existe no dicionário e exibe a cidade correspondente
if ddd_usuario in ddd:
    print(ddd[ddd_usuario])
else:
    print("DDD nao cadastrado")
