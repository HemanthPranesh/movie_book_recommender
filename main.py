from recommender import ContentRecommender
#Main block
if __name__ == "__main__":
    rec = ContentRecommender("data.csv")
    fav = input("Enter your favorite movie/book: ")
    print("\nTop 5 Recommendations:")
    for r in rec.recommend(fav):
        print("-", r)
