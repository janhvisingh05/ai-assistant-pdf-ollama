from rag.embedder import get_embeddings
from rag.vectordb import query

def retrieve_context(query_text):
    query_embedding = get_embeddings([query_text])[0]
    docs = query(query_embedding)
    return "\n".join(docs)