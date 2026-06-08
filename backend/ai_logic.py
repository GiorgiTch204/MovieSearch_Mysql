import json

import numpy as np
from sentence_transformers import SentenceTransformer

from backend.db import get_connection


print("Loading AI model...")
model = SentenceTransformer("all-MiniLM-L6-v2")


def cosine_similarity(vector_a, vector_b):
    a = np.array(vector_a, dtype=np.float32)
    b = np.array(vector_b, dtype=np.float32)

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return float(np.dot(a, b) / denominator)


def search_movies(query, top_k=10):
    query_embedding = model.encode(query).tolist()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, title, overview, embedding FROM movies")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    results = []

    for row in rows:
        movie_embedding = json.loads(row["embedding"])
        score = cosine_similarity(query_embedding, movie_embedding)

        results.append({
            "title": row["title"],
            "overview": row["overview"],
            "score": round(score, 4)
        })

    results.sort(key=lambda item: item["score"], reverse=True)

    return results[:top_k]


if __name__ == "__main__":
    print(search_movies("space exploration and black holes", top_k=5))