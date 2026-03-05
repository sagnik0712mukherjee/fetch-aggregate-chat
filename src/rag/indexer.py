import faiss
from src.rag.embedder import embed_text


def index_faiss_docs(docs):
    try:
        doc_embeddings = embed_text(docs)
        dimension = doc_embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)
        index.add(doc_embeddings)
        return index
    except Exception as e:
        raise RuntimeError(f"[Index Error] Failed to create FAISS index: {str(e)}")
