import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tmdb_api import search_movie

class ContentRecommender:
    def __init__(self, movies):
        self.movies = pd.DataFrame(movies)
        self.prepare()

    def prepare(self):
        if self.movies.empty:
            return
        self.movies['content'] = (
            self.movies['title'].fillna('') + " " +
            self.movies['overview'].fillna('') + " " +
            self.movies['release_date'].fillna('')
        )
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.movies['content'])
        self.similarity = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def recommend(self, title, top_n=5):
        # if title not in current dataset, fetch from TMDb
        if title not in self.movies['title'].values:
            results = search_movie(title)
            if results:
                movie = results[0]  # best match
                self.movies = pd.concat([self.movies, pd.DataFrame([movie])], ignore_index=True)
                self.prepare()
                title = movie['title']
            else:
                return []

        idx = self.movies[self.movies['title'] == title].index[0]
        scores = list(enumerate(self.similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        return self.movies.iloc[[i[0] for i in scores]][
            ['title', 'overview', 'release_date', 'poster_path']
        ]
