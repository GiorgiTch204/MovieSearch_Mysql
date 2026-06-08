# MovieSearch MySQL

MovieSearch is a semantic movie search web application that allows users to search for movies using natural language descriptions instead of exact movie titles or exact keywords.

This version of the project uses **FastAPI**, **Sentence-BERT**, and **MySQL**. Movie descriptions are converted into vector embeddings and stored in a MySQL database. When the user searches for a movie, the query is also converted into an embedding, compared with stored movie embeddings, and the most semantically similar movies are returned.

---

## Project Idea

Traditional search systems usually depend on exact keyword matching. This can be limited when users do not remember the exact movie title or do not use the same words that exist in the movie description.

MovieSearch solves this problem by using semantic search.

Example queries:

```text
space exploration and black holes
sad animated movie with a robot
a man fighting crime in a dark costume
romantic movie about memories and love
```

The system searches based on meaning and context, not only exact words.

---

## Technologies Used

### Backend

```text
Python
FastAPI
Uvicorn
Sentence-Transformers
Sentence-BERT
MySQL Connector
NumPy
Pandas
```

### Frontend

```text
HTML5
Tailwind CSS
JavaScript
Fetch API
```

### Database

```text
MySQL
Azure Database for MySQL Flexible Server
```

### AI / NLP Model

```text
all-MiniLM-L6-v2
```

---

## Project Structure

```text
MovieSearch_Mysql/
│
├── backend/
│   ├── __init__.py
│   ├── ai_logic.py
│   ├── db.py
│   ├── import_movies.py
│   └── requirements.txt
│
├── data/
│   └── .gitkeep
│
├── frontend/
│   ├── index.html
│   └── script.js
│
├── main.py
├── requirements.txt
├── run.bat
├── README.md
├── .gitignore
└── .env.example
```

---

## How the System Works

The system works in two main phases.

### 1. Data Import Phase

```text
TMDB 5000 Movie Dataset
        ↓
Pandas reads CSV file
        ↓
Movie title and overview are extracted
        ↓
Sentence-BERT creates embeddings
        ↓
Embeddings are stored in MySQL as JSON
```

### 2. Search Phase

```text
User writes a natural language query
        ↓
Frontend sends request to FastAPI
        ↓
FastAPI calls semantic search logic
        ↓
Sentence-BERT creates query embedding
        ↓
Python calculates cosine similarity
        ↓
Top matching movies are returned
        ↓
Frontend displays movie cards
```

---

## Database Structure

The project uses a MySQL table named `movies`.

```sql
CREATE TABLE movies (
    id INT PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    overview TEXT NOT NULL,
    embedding JSON NOT NULL
);
```

The `embedding` column stores the vector representation of the movie overview as JSON.

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
MYSQL_HOST=moviesearch-mysql.mysql.database.azure.com
MYSQL_PORT=3306
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=moviesearch_db
```

Do not upload `.env` to GitHub.

Use `.env.example` as a template.

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/GiorgiTch204/MovieSearch_Mysql.git
cd MovieSearch_Mysql
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

On Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## MySQL Database Setup

Create a database:

```sql
CREATE DATABASE moviesearch_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Use the database:

```sql
USE moviesearch_db;
```

Create the movies table:

```sql
CREATE TABLE movies (
    id INT PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    overview TEXT NOT NULL,
    embedding JSON NOT NULL
);
```

---

## Dataset Note

This project uses the **TMDB 5000 Movie Dataset**.

Dataset link:

```text
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
```

The dataset file is not uploaded to GitHub because it can be large.

Download the dataset and place the CSV file here:

```text
data/tmdb_5000_movies.csv
```

The application expects the following columns:

```text
id
original_title
overview
```

---

## Import Movies into MySQL

After configuring the database and placing the dataset file inside the `data/` folder, run:

```bash
python -m backend.import_movies
```

This command:

```text
1. Reads the CSV dataset
2. Loads the Sentence-BERT model
3. Generates embeddings for movie overviews
4. Stores movies and embeddings in MySQL
```

After import, check the database:

```sql
SELECT COUNT(*) FROM movies;
SELECT id, title FROM movies LIMIT 5;
```

---

## Run the FastAPI Server

Start the backend server:

```bash
python -m uvicorn main:app --reload
```

API root:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run the Frontend

Open this file in the browser:

```text
frontend/index.html
```

The frontend sends search requests to:

```text
http://127.0.0.1:8000/search
```

---

## Example API Request

```text
http://127.0.0.1:8000/search?query=space exploration and black holes&limit=10
```

Example response:

```json
{
  "results": [
    {
      "title": "Interstellar",
      "overview": "Movie overview text...",
      "score": 0.8421
    }
  ]
}
```

---

## Run with run.bat

On Windows, you can start the project using:

```text
run.bat
```

The batch file can start the FastAPI server, open Swagger documentation, and open the frontend page.

---

## Azure MySQL Hosting

The MySQL database can be hosted using:

```text
Azure Database for MySQL Flexible Server
```

For Azure MySQL, use the Azure database endpoint in `.env`:

```env
MYSQL_HOST=moviesearch-mysql.mysql.database.azure.com
MYSQL_PORT=3306
MYSQL_USER=your_azure_mysql_user
MYSQL_PASSWORD=your_azure_mysql_password
MYSQL_DATABASE=moviesearch_db
```

Before connecting from local machine or backend server, make sure the Azure MySQL firewall allows your IP address.

---

## Important Security Notes

Do not upload these files/folders to GitHub:

```text
venv/
.env
data/tmdb_5000_movies.csv
__pycache__/
```

The `.env` file contains private database credentials and must stay local.

---

## Current Version Notes

This is an experimental MySQL version of MovieSearch.

The original thesis-safe version uses ChromaDB for vector search. This MySQL version stores embeddings in MySQL and calculates cosine similarity in Python.

For small datasets such as TMDB 5000, this approach is acceptable for experimentation and learning database-based architecture.

---

## Future Improvements

Possible future improvements:

```text
React or Next.js frontend
Movie posters and metadata
Search history
User favorites
Hybrid search: keyword + semantic search
Cloud deployment of FastAPI backend
Vector search support using a specialized vector database
```

---

## Author

```text
Giorgi Cheishvili
Bachelor Thesis Project
Computer Science
MovieSearch
```
