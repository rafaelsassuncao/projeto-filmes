import requests

# Chave da API do TMDb
API_KEY = 'd58f6221d83c014154371dfd5a4d3380'

# Função para buscar detalhes de um filme pelo ID
def buscar_detalhes_filme(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'
    resposta = requests.get(url)
    return resposta.json()

# Função para buscar o elenco de um filme pelo ID
def buscar_elenco_filme(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}'
    resposta = requests.get(url)
    return resposta.json()

# Lista de IDs dos filmes que queremos analisar
lista_filmes = [550, 551, 552]

# Dicionários para armazenar os dados
participacao_atores = {}  
frequencia_generos = {}  
bilheteria_atores = {}  

# Percorre cada filme da lista
for movie_id in lista_filmes:
    detalhes = buscar_detalhes_filme(movie_id)
    elenco = buscar_elenco_filme(movie_id)

    # Conta a participação dos atores e a bilheteria
    if 'cast' in elenco:
        for ator in elenco['cast']:
            nome_ator = ator['name']
            if nome_ator in participacao_atores:
                participacao_atores[nome_ator] += 1
                bilheteria_atores[nome_ator] += detalhes.get('revenue', 0)
            else:
                participacao_atores[nome_ator] = 1
                bilheteria_atores[nome_ator] = detalhes.get('revenue', 0)

    # Conta a frequência dos gêneros
    if 'genres' in detalhes:
        for genero in detalhes['genres']:
            nome_genero = genero['name']
            if nome_genero in frequencia_generos:
                frequencia_generos[nome_genero] += 1
            else:
                frequencia_generos[nome_genero] = 1

# Exibe os resultados
print("Participação dos Atores:")
for ator, participacao in participacao_atores.items():
    print(f"{ator}: {participacao} filmes")

print("\nFrequência dos Gêneros:")
for genero, frequencia in frequencia_generos.items():
    print(f"{genero}: {frequencia} filmes")

# Top 5 Atores com Maior Bilheteria
print("\nTop 5 Atores com Maior Bilheteria:")
# Ordena os atores por bilheteria (do maior para o menor)
top_5_atores = sorted(bilheteria_atores.items(), key=lambda x: x[1], reverse=True)[:5]
for ator, bilheteria in top_5_atores:
    print(f"{ator}: ${bilheteria:,.2f}")