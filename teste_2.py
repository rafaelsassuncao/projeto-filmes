import requests

# Chave da API do TMDb
API_KEY = "d58f6221d83c014154371dfd5a4d3380"

# Função para buscar detalhes de um filme pelo ID
def buscar_detalhes_filme(movie_id):
  url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'
  resposta = requests.get(url)
  return resposta.json()

# Função para buscar filmes similares pelo ID
def buscar_filmes_similares(movie_id):
  url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'
  resposta = requests.get(url)
  return resposta.json()

# Função para recomendar filmes baseados em critérios
def recomendar_filmes(movie_id):
  detalhes_filmes = buscar_detalhes_filme(movie_id)
  filmes_similares = buscar_filmes_similares(movie_id)

  if 'results' in filmes_similares
