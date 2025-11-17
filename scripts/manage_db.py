import psycopg2
from processing.generate_embeddings import generate_embedding
from processing.chunk_text import chunk_text

conn = psycopg2.connect(
    dbname="askit_db",
    user="rag_user",
    password="rag_pass",
    host="db",
    port="5432"
)
cur = conn.cursor()

def add_text(title, content):
    insert_query_text = """
    INSERT INTO texts (title, content)
    VALUES (%s, %s)
    RETURNING id;
    """
    cur.execute(insert_query_text, (title, content))
    text_id = cur.fetchone()[0]

    insert_query_chunk = """
    INSERT INTO text_chunks (text_id, start_offset, end_offset, embedding, model_name)
    VALUES (%s, %s, %s, %s, %s)
    """

    for chunk in chunk_text(content):
        cur.execute(insert_query_chunk, (text_id, chunk[0], chunk[1], chunk[2], chunk[3]))

    conn.commit()
    return text_id

def remove_text(text_id):
    delete_query = "DELETE FROM texts WHERE id = %s;"
    cur.execute(delete_query, (text_id,))
    conn.commit()

def query_similar_chunks(embedding, top_k=5):
    query = """
    SELECT
        t.title,
        t.content,
        tc.start_offset,
        tc.end_offset,
        tc.embedding <-> %s::vector AS distance
    FROM text_chunks AS tc
    JOIN texts AS t ON tc.text_id = t.id
    ORDER BY distance
    LIMIT %s;
    """
    cur.execute(query, (embedding, top_k))
    return cur.fetchall()

def query_similar_chunks_by_text(text, top_k=5):
    embedding = generate_embedding(text)
    return query_similar_chunks(embedding, top_k)

def get_all_texts():
    query = "SELECT text_id, start_offset, end_offset FROM text_chunks;"
    cur.execute(query)
    return cur.fetchall()