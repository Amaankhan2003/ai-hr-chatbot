# AI-Powered HR Chatbot (RAT-Based)

## Overview
This project is an AI-powered HR chatbot designed to answer employee queries using
Retrieval-Augmented Transformer (RAT) architecture.

The chatbot retrieves relevant information from HR policy documents and generates
accurate, policy-grounded responses using an LLM.

## Features
- Semantic search using FAISS
- Retrieval-Augmented Answer Generation (RAT)
- Strictly policy-based answers (no hallucinations)
- Secure API key handling
- Modular and extensible design

## Tech Stack
- Python
- Sentence Transformers
- FAISS
- OpenAI API
- dotenv

## Project Structure
chatbot/        → RAT chatbot logic
ingestion/      → Document extraction & cleaning
embeddings/     → Vector indexing & metadata
data/           → HR policy documents

## How to Run
1. Create virtual environment
2. Install dependencies
3. Add `.env` with OpenAI API key
4. Run ingestion → embeddings → chatbot

## Future Enhancements
- Web UI (FastAPI + React)
- Slack integration
- Role-based access
- Audit logs
