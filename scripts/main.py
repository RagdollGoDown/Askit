from manage_db import add_text, query_similar_chunks_by_text, get_all_texts, remove_text

def main():
    query_text = "What protocol is connectionless and does not provide acknowledgments?"

    print("Similar chunks for query:", query_similar_chunks_by_text(query_text, top_k=3))

    all_texts = get_all_texts()

    print("All texts:", all_texts)

if __name__ == "__main__":
    main()