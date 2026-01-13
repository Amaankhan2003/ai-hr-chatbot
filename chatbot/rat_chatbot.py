import json
import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------
# Load environment variables
# -----------------------
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=OPENAI_API_KEY)

# -----------------------
# Paths
# -----------------------
INDEX_PATH = "embeddings/faiss_index.bin"
METADATA_PATH = "embeddings/metadata.json"

if not os.path.exists(INDEX_PATH):
    raise FileNotFoundError("FAISS index not found. Run Phase 3 first.")
if not os.path.exists(METADATA_PATH):
    raise FileNotFoundError("metadata.json not found. Run Phase 3 first.")

# -----------------------
# Load FAISS + metadata
# -----------------------
index = faiss.read_index(INDEX_PATH)

with open(METADATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [d["text"] for d in data]

# -----------------------
# Embedding model
# -----------------------
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
TOP_K = 3

# -----------------------
# Retrieval
# -----------------------
def retrieve_chunks(query, k=TOP_K):
    query_vec = embed_model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, k)

    chunks = []
    for idx in indices[0]:
        if idx < len(texts):
            chunks.append(texts[idx])
    return chunks

# -----------------------
# RAT Answer Generation
# -----------------------
def generate_answer(query):
    chunks = retrieve_chunks(query)

    if not chunks:
        return "I am sorry, I don't have that information."

    context = "\n\n".join(chunks)

    system_prompt = (
        "You are an HR assistant chatbot.\n"
        "Answer ONLY using the HR policy context provided.\n"
        "If the answer is not explicitly present, reply exactly:\n"
        "'I am sorry, I don't have that information.'"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0,
            max_tokens=300,
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"HR Policy Context:\n{context}\n\nQuestion: {query}"
                }
            ],
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"LLM Error: {e}"

# -----------------------
# CLI Chat Loop
# -----------------------
def chat_loop():
    print("HR RAT Chatbot (Phase 4). Type 'exit' to quit.\n")
    while True:
        query = input("You: ").strip()
        if query.lower() == "exit":
            break
        answer = generate_answer(query)
        print(f"Chatbot: {answer}\n")

# -----------------------
# Run
# -----------------------
if __name__ == "__main__":
    chat_loop()
