import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "embeddings/faiss_index.bin"
METADATA_PATH = "embeddings/metadata.json"

def main():
    # Load FAISS index
    index = faiss.read_index(INDEX_PATH)

    # Load metadata
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [d["text"] for d in data]
    metadata = [d["metadata"] for d in data]

    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    while True:
        query = input("\nAsk a HR question (or type 'exit'): ").strip()
        if query.lower() == "exit":
            break

        query_vec = model.encode([query]).astype("float32")

        distances, indices = index.search(query_vec, k=3)

        print("\nTop results:\n")
        for rank, idx in enumerate(indices[0]):
            print(f"Result {rank + 1}")
            print(f"Policy: {metadata[idx]['policy']}")
            print(f"Source: {metadata[idx]['source']}")
            print(f"Text: {texts[idx][:300]}...")
            print("-" * 50)

if __name__ == "__main__":
    main()
