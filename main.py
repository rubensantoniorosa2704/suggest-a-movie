
import pandas as pd
from flask import Flask, request, jsonify

# Carregar a base de dados
df = pd.read_csv('tmdb_5000_movies.csv')

# Selecionar atributos para o sistema RBC
selected_attributes = ['genres', 'keywords', 'original_language', 'popularity', 'vote_average']

# Definir funções de similaridade para cada atributo
def genre_similarity(genres1, genres2):
    set1 = set(genres1)
    set2 = set(genres2)
    return len(set1.intersection(set2)) / len(set1.union(set2))

def keyword_similarity(keywords1, keywords2):
    set1 = set(keywords1)
    set2 = set(keywords2)
    return len(set1.intersection(set2)) / len(set1.union(set2))

def language_similarity(lang1, lang2):
    return 1 if lang1 == lang2 else 0

def popularity_similarity(pop1, pop2):
    return 1 - abs(pop1 - pop2) / max(pop1, pop2)

def vote_similarity(vote1, vote2):
    return 1 - abs(vote1 - vote2) / 10

# Definir pesos para cada atributo
weights = {
    'genres': 0.3,
    'keywords': 0.3,
    'original_language': 0.1,
    'popularity': 0.15,
    'vote_average': 0.15
}

# Calcular similaridade geral
def calculate_similarity(movie1, movie2):
    similarity = (
        weights['genres'] * genre_similarity(movie1['genres'], movie2['genres']) +
        weights['keywords'] * keyword_similarity(movie1['keywords'], movie2['keywords']) +
        weights['original_language'] * language_similarity(movie1['original_language'], movie2['original_language']) +
        weights['popularity'] * popularity_similarity(movie1['popularity'], movie2['popularity']) +
        weights['vote_average'] * vote_similarity(movie1['vote_average'], movie2['vote_average'])
    )
    return similarity

# Criar aplicação Flask
app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie_id = data.get('movie_id')

    # Encontrar o filme na base de dados
    movie = df[df['id'] == movie_id].iloc[0]

    # Calcular similaridade com todos os outros filmes
    df['similarity'] = df.apply(lambda x: calculate_similarity(movie, x), axis=1)

    # Excluir o próprio filme da lista de recomendações
    recommendations = df[df['id'] != movie_id]

    # Obter as 5 principais recomendações
    recommendations = recommendations.sort_values(by='similarity', ascending=False).head(5)[['title', 'similarity']]

    # Retornar recomendações como JSON
    return jsonify(recommendations.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
