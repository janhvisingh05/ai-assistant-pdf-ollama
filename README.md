# 🧠 AI Assistant (RAG + Memory + Guardrails + Ollama)

A fully local AI assistant that answers questions from your documents using **Retrieval-Augmented Generation (RAG)**, enhanced with **chat memory** and **multi-layer guardrails**.

---

## 🚀 Features

* 🔍 **RAG Pipeline** – Retrieves relevant document chunks before answering
* 🧠 **Chat Memory** – Stores conversation history (SQLite)
* 🛡️ **Guardrails System**

  * Input validation
  * Context relevance filtering
  * Output safety checks
* 🤖 **Local LLM** – Runs using Ollama (no API required)
* 📄 **PDF-based Knowledge**
* 💻 **Streamlit UI**

---

## 🏗️ Architecture

```
User Query
   ↓
Input Guard
   ↓
Memory (Chat History)
   ↓
Retriever (Top-K Chunks)
   ↓
Context Guard
   ↓
LLM (Ollama - gemma2:2b)
   ↓
Output Guard
   ↓
Final Response + DB Storage
```

---

## ⚙️ Tech Stack

| Component    | Technology                     |
| ------------ | ------------------------------ |
| Frontend     | Streamlit                      |
| Backend      | Python                         |
| LLM          | Ollama (gemma2:2b)             |
| Embeddings   | sentence-transformers (MiniLM) |
| Vector Store | ChromaDB                       |
| Database     | SQLite                         |
| Guardrails   | Custom Python modules          |

---

## 📂 Project Structure

```
ai_assistant_project/
│
├── app.py
├── config.py
├── requirements.txt
│
├── database/
│   ├── db.py
│   └── schema.sql
│
├── guardrails/
│   ├── input_guard.py
│   ├── context_guard.py
│   └── output_guard.py
│
├── llm/
│   └── ollama.py
│
├── rag/
│   ├── embedder.py
│   ├── ingest.py
│   ├── pdf_loader.py
│   ├── retriever.py
│   └── vectordb.py
│
└── utils/
    └── memory.py
```

---

## 🧪 How to Run (Local Setup)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/janhvisingh05/ai-assistant-pdf-ollama.git
cd ai-assistant-pdf-ollama
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install Ollama

Download and install from:
👉 https://ollama.com

---

### 5️⃣ Pull the model

```bash
ollama pull gemma2:2b
```

---

### 6️⃣ Start Ollama (if not already running)

```bash
ollama serve
```

> If you see a port error, it means Ollama is already running.

---

### 7️⃣ Run the app

```bash
streamlit run app.py
```

---

### 8️⃣ Open in browser

```
http://localhost:8501
```

---

## 📄 How It Works

1. User enters a query
2. Input guard validates it
3. Chat history is fetched
4. Relevant document chunks are retrieved
5. Context guard filters irrelevant data
6. Ollama generates answer
7. Output guard ensures safety
8. Response is stored and displayed

---

## 🛡️ Guardrails Explained

| Guard Type    | Purpose                                  |
| ------------- | ---------------------------------------- |
| Input Guard   | Blocks unsafe or invalid queries         |
| Context Guard | Ensures retrieved data is relevant       |
| Output Guard  | Prevents low-quality or unsafe responses |

---

## 📌 Notes

* Fully **offline system** (no API keys required)
* Works on **local CPU/GPU**
* Optimized for **small to medium document sets**

---

## ⚠️ Limitations

* Local models may be slower than cloud LLMs
* Accuracy depends on document quality
* Large datasets require optimization (FAISS recommended)

---

## 🚀 Future Improvements

* Streaming responses
* FastAPI backend (production scaling)
* Multi-document upload UI
* Better vector search (FAISS)
* Role-based memory


## 👩‍💻 Author

**Janhvi Singh**

---

## ⭐ If you found this useful, consider starring the repo!
