from recommender import ContentRecommender

if __name__ == "__main__":
    # Initialize recommender
    rec = ContentRecommender("data.csv")

    # Ask user input
    fav = input("Enter your favorite movie/book: ")
    print("\nTop 5 Recommendations:")
    for r in rec.recommend(fav):
        print("-", r)
