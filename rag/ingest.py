import os
from rag.pdf_loader import load_pdf
from rag.embedder import get_embeddings
from rag.vectordb import add_documents
from config import UPLOAD_DIR

def chunk_text(text, chunk_size=800, overlap=150):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        # Clean text
        chunk = chunk.replace("\n", " ")
        chunk = " ".join(chunk.split())

        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

def ingest_pdfs():
    all_chunks = []

    for file in os.listdir(UPLOAD_DIR):
        if file.endswith(".pdf"):
            path = os.path.join(UPLOAD_DIR, file)
            print(f"Ingesting: {file}")

            text = load_pdf(path)
            chunks = chunk_text(text)

            # Add source metadata
            chunks = [f"[SOURCE: {file}] {c}" for c in chunks]

            all_chunks.extend(chunks)

    if all_chunks:
        print(f"Total chunks: {len(all_chunks)}")

        embeddings = get_embeddings(all_chunks)
        add_documents(all_chunks, embeddings)

        print("✅ Multilingual PDFs indexed successfully!")
    else:
        print("⚠️ No PDFs found.")

if __name__ == "__main__":
    ingest_pdfs()