import os
import json

PROCESSED_DIR = "data/hr_docs/processed"
CHUNKS_DIR = "data/hr_docs/chunks"

CHUNK_SIZE = 400
OVERLAP = 80

os.makedirs(CHUNKS_DIR, exist_ok=True)

def chunk_text(text, chunk_size=400, overlap=80):
    words = text.split()

    if len(words) == 0:
        return []

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk = " ".join(chunk_words).strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

def infer_policy_name(filename):
    return filename.replace("_", " ").replace(".txt", "").title()

def main():
    all_chunks = []

    for filename in os.listdir(PROCESSED_DIR):
        file_path = os.path.join(PROCESSED_DIR, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().strip()

        if not text:
            print(f"[SKIP] Empty processed file → {filename}")
            continue

        chunks = chunk_text(text)

        if len(chunks) == 0:
            print(f"[WARN] No chunks created for → {filename}")
            continue

        policy_name = infer_policy_name(filename)

        for idx, chunk in enumerate(chunks):
            all_chunks.append({
                "id": f"{policy_name}_{idx}",
                "text": chunk,
                "metadata": {
                    "policy": policy_name,
                    "source": filename
                }
            })

        print(f"[OK] Chunked → {filename} ({len(chunks)} chunks)")

    output_path = os.path.join(CHUNKS_DIR, "chunks.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2)

    print(f"\n[SUCCESS] Total chunks saved → {output_path}")

if __name__ == "__main__":
    main()
