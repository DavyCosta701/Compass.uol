import requests
import pandas as pd
from config import API_KEY

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=pt-BR"

response = requests.get(url=url)
data = response.json()

filmes = [
    {'Titulo': movie['title'],
    'Data de lançamento': movie['release_date'],
    'Visão geral': movie['overview'],
    'Votos': movie['vote_count'],
    'Média de votos:': movie['vote_average']} for movie in data['results']
]

df = pd.DataFrame(filmes)
print(df)

