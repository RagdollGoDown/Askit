from .generate_embeddings import generate_embedding, model_name


def chunk_text(text, chunk_size=500, overlap=50):
    """
    Generates text chunks from the text param. Going sentence by sentence.

    Returns:
    chunks: a list of [start, end, embedding, model name]

    """

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk_text = text[start:end]
        embedding = generate_embedding(chunk_text)
        chunks.append([start, end, embedding, model_name])
        start += chunk_size - overlap

    print(f"Text chunked into {len(chunks)} chunks.")

    return chunks