import os
import re

PROCESSED_DIR = "data/hr_docs/processed"

def clean_text(text):
    # Remove page numbers
    text = re.sub(r"Page\s+\d+", "", text, flags=re.IGNORECASE)

    # Remove excessive whitespace
    text = re.sub(r"\n{2,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    # Remove common footer/header words
    junk_patterns = [
        r"Confidential",
        r"Company Internal Use Only"
    ]
    for pattern in junk_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)

    return text.strip()

def main():
    for filename in os.listdir(PROCESSED_DIR):
        file_path = os.path.join(PROCESSED_DIR, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        cleaned = clean_text(raw_text)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(cleaned)

        print(f"[OK] Cleaned → {filename}")

if __name__ == "__main__":
    main()
