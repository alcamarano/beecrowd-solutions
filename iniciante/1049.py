# Dicionário - árvore de decisão: tipo → classe → dieta → animal
animais = {
    "vertebrado": {
        "ave":      {"carnivoro": "aguia",       "onivoro": "pomba"},
        "mamifero": {"onivoro":   "homem",        "herbivoro": "vaca"},
    },
    "invertebrado": {
        "inseto":   {"hematofago": "pulga",       "herbivoro": "lagarta"},
        "anelideo": {"hematofago": "sanguessuga", "onivoro":   "minhoca"},
    },
}
# Ler os valores do usuário
a = input().lower()
b = input().lower()
c = input().lower()
# Busca o animal percorrendo os três níveis do dicionário e apresenta o resultado
print(animais[a][b][c])
