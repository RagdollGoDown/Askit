from sentence_transformers import SentenceTransformer

model_name = 'nomic-ai/nomic-embed-text-v1.5'

model = SentenceTransformer(
    model_name, 
    trust_remote_code=True
)

def generate_embedding(text):
    embedding = model.encode(text)
    return embedding.tolist()