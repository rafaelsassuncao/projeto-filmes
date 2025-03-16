import requests
from collections import defaultdict

API_KEY = 'd58f6221d83c014154371dfd5a4d3380'

def buscas_detalhes_filmes(movie_id):
  url = f'https://www.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'
  response = requests.get(url)
  return response.json()

def busca_elenco_detalhes(movie_id):
  url = f'https://www.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'
  response = requests.get(url)
  return response.json()

# Lista de Filmes (ID)
lista_filmes = [550, 551, 552]

participacao_atores = defaultdict(int)
frequencia_generos = defaultdict(int)
bilheteria_atores = defaultdict(float)

# Percorre cada filme da lista
for movie_id in lista_filmes:
  detalhes = buscas_detalhes_filmes(movie_id)
  elenco = busca_elenco_detalhes(movie_id)

for ator in elenco ['cast']:
  participacao_atores[ator['name']] += 1

for genero in detalhes['genres']:
  frequencia_generos[genero['name']] += 1

for ator in elenco['cast']:
  bilheteria_atores[ator['name']] += detalhes['revenue']




