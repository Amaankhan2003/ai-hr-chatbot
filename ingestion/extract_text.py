import os
from pypdf import PdfReader
from docx import Document

RAW_DIR = "data/hr_docs/raw"
PROCESSED_DIR = "data/hr_docs/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

def extract_pdf(path):
    reader = PdfReader(path)
    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    return "\n".join(text)

def extract_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

def extract_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    for filename in os.listdir(RAW_DIR):
        file_path = os.path.join(RAW_DIR, filename)

        if filename.endswith(".pdf"):
            text = extract_pdf(file_path)
        elif filename.endswith(".docx"):
            text = extract_docx(file_path)
        elif filename.endswith(".txt"):
            text = extract_txt(file_path)
        else:
            continue

        output_file = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(PROCESSED_DIR, output_file)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"[OK] Extracted → {output_file}")

if __name__ == "__main__":
    main()
