import requests

API_KEY = "20bd51a1afa9d7ba7a5a1862a808a3bb"  
BASE_URL = "https://api.themoviedb.org/3"

def get_popular_movies(page=1):
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
    response = requests.get(url)
    return response.json().get("results", [])

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    return response.json()

def search_movie(query):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&language=en-US&query={query}"
    response = requests.get(url)
    return response.json().get("results", [])
