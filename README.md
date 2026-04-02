# 🧠 AI Assistant (RAG + Memory + Guardrails + Ollama)

A fully local AI assistant that answers questions from documents using Retrieval-Augmented Generation (RAG), with chat memory and safety guardrails.

---

## 🚀 Features

- 🔍 RAG-based document retrieval
- 🧠 Chat memory (SQLite)
- 🛡️ Guardrails:
  - Input validation
  - Context relevance check
  - Output filtering
- 🤖 Local LLM using Ollama (gemma2:2b)
- 💻 Streamlit UI

---

## 🏗️ Architecture

User Query  
→ Input Guard  
→ Memory (chat history)  
→ Retriever (top-k chunks)  
→ Context Guard  
→ LLM (Ollama)  
→ Output Guard  
→ Response  

---

## ⚙️ Tech Stack

- Frontend: Streamlit  
- Backend: Python  
- LLM: Ollama (gemma2:2b)  
- Embeddings: sentence-transformers (MiniLM)  
- DB: SQLite  
- Vector Store: ChromaDB  

---

## 🧪 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
