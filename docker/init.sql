CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE texts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL UNIQUE,
    content TEXT NOT NULL,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE text_chunks (
    id SERIAL PRIMARY KEY,

    text_id INT REFERENCES texts(id) ON DELETE CASCADE,
    start_offset INT,
    end_offset INT,

    embedding VECTOR(768) NOT NULL,
    model_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE INDEX idx_text_chunks_embedding ON text_chunks USING ivfflat (embedding vector_l2_ops) WITH (lists = 100);
CREATE INDEX idx_texts_title ON texts (title);