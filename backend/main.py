from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    user_input: str
    category: str

@app.get("/")
def read_root():
    return {"message": "Movie/Book Recommender API running with Llama3"}

@app.post("/recommend")
def recommend_movies(query: Query):
    try:
        user_input = query.user_input
        category = query.category

        if category == "movie":
            prompt = f"Recommend 5 movies for: {user_input}. Format: Movie - reason"
        else:
            prompt = f"Recommend 5 books for: {user_input}. Format: Book - reason"

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        result = data.get("response", "No response from model")

        return {"recommendations": result}

    except Exception as e:
        return {"recommendations": f"Error: {str(e)}"}
