from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.ai_logic import search_movies


app = FastAPI(title="Movie Semantic Search API - MySQL Version")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "MovieSearch MySQL API is running!"}


@app.get("/search")
def search(query: str, limit: int = 10):
    results = search_movies(query, top_k=limit)
    return {"results": results}