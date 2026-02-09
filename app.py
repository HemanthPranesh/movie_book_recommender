from flask import Flask, render_template, request
from recommender import ContentRecommender
from tmdb_api import get_popular_movies

app = Flask(__name__)

movies = get_popular_movies(page=1)
recommender = ContentRecommender(movies)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    if request.method == "POST":
        movie_name = request.form["movie"]
        recommendations = recommender.recommend(movie_name, top_n=5).to_dict(orient="records")
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
