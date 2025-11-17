from manage_db import add_text, query_similar_chunks_by_text, get_all_texts, remove_text

from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "Hey there!"}
