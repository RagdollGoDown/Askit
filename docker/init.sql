-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Example table for Wikipedia text chunks
CREATE TABLE IF NOT EXISTS wiki_chunks (
    id SERIAL PRIMARY KEY,
    title TEXT,
    chunk_id INT,
    content TEXT,
    embedding VECTOR(1536)  -- Use 1536 if you're using OpenAI embeddings
);
