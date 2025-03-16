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
Lista_filmes = [550, 551, 552]





