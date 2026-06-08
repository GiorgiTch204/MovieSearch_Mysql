import os
import json

import pandas as pd
from sentence_transformers import SentenceTransformer

from backend.db import get_connection


def load_dataset():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "tmdb_5000_movies.csv")

    df = pd.read_csv(csv_path)
    df = df[["id", "original_title", "overview"]].dropna()

    return df


def import_movies():
    print("Loading dataset...")
    df = load_dataset()

    print("Loading Sentence-BERT model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    conn = get_connection()
    cursor = conn.cursor()

    print("Clearing old movies...")
    cursor.execute("DELETE FROM movies")
    conn.commit()

    titles = df["original_title"].tolist()
    overviews = df["overview"].tolist()
    ids = df["id"].tolist()

    print("Creating embeddings. Please wait...")
    embeddings = model.encode(overviews)

    print("Inserting movies into MySQL...")

    insert_query = """
        INSERT INTO movies (id, title, overview, embedding)
        VALUES (%s, %s, %s, %s)
    """

    for movie_id, title, overview, embedding in zip(ids, titles, overviews, embeddings):
        cursor.execute(
            insert_query,
            (
                int(movie_id),
                str(title),
                str(overview),
                json.dumps(embedding.tolist())
            )
        )

    conn.commit()
    cursor.close()
    conn.close()

    print("Import completed successfully!")


if __name__ == "__main__":
    import_movies()