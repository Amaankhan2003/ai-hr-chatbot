# AI-Powered HR Chatbot

An AI-powered HR Chatbot that answers employee questions based on provided HR policies and documents.  
Built using **Python**, **FastAPI**, **RAT (Retrieval-Augmented Transformer)**, and **FAISS embeddings**.  
Includes a **web-based chat interface** for seamless interaction.

---

## Features

- Understands simple English employee queries
- Provides accurate answers strictly from HR documents
- Reduces repetitive queries to HR teams
- Local and secure setup — all data stays on your machine
- Modern web UI for chat-like interaction
- Retrieval-Augmented Transformer (RAT) architecture for context-aware answers
- FAISS semantic search for fast document retrieval

---

## Project Structure

hr-chatbot/
├── api/ # FastAPI backend
│ └── main.py
├── chatbot/ # RAT + LLM logic
│ └── rat_chatbot.py
├── ingestion/ # Preprocessing scripts
│ ├── extract_text.py
│ ├── clean_text.py
│ └── chunk_documents.py
├── embeddings/ # FAISS index creation
│ └── faiss_index.py
├── data/ # HR documents and chunks
│ └── hr_docs/
│ ├── raw/
│ ├── processed/
│ └── chunks/
├── ui/ # Web interface
│ └── index.html
├── requirements.txt
└── README.md


---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Amaankhan2003/ai-hr-chatbot.git
cd ai-hr-chatbot
```
## Usage

Ask questions like:

- "How many casual leaves do I have?"

- "What is the attendance policy?"

- "Can I work from home on Fridays?"

- The chatbot will answer strictly based on HR documents.

If an answer is not found, it replies:
"That information is not mentioned in the HR policy."

## Technologies Used

- Python 3.10+

- FastAPI (Backend API)

- RAT (Retrieval-Augmented Transformer)

- FAISS (Vector database for semantic search)

- Sentence Transformers (Embedding model)

- OpenAI GPT-4o-mini (LLM for answer generation)

- HTML, CSS, JS (Web chat interface)

## DEMO OF THE VIDEO
https://drive.google.com/uc?id=14NEKJNRWu32Xah2AfvKU_AxQdAd9qDbd&export=download
