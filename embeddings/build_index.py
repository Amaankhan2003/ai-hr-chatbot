import json
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNKS_PATH = "data/hr_docs/chunks/chunks.json"
INDEX_PATH = "embeddings/faiss_index.bin"
METADATA_PATH = "embeddings/metadata.json"

os.makedirs("embeddings", exist_ok=True)

def main():
    # Load chunks
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    if not chunks:
        raise ValueError("No chunks found. Phase 2 might be broken.")

    texts = [c["text"] for c in chunks]
    metadata = [c["metadata"] for c in chunks]

    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("[INFO] Generating embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True)

    embeddings = np.array(embeddings).astype("float32")

    # Create FAISS index
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    # Save index
    faiss.write_index(index, INDEX_PATH)

    # Save metadata
    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(
            [{"text": texts[i], "metadata": metadata[i]} for i in range(len(texts))],
            f,
            indent=2
        )

    print(f"[SUCCESS] FAISS index saved → {INDEX_PATH}")
    print(f"[SUCCESS] Metadata saved → {METADATA_PATH}")
    print(f"[INFO] Total vectors indexed → {index.ntotal}")

if __name__ == "__main__":
    main()
