import faiss
from src.rag.embedder import embed_text

def index_faiss_docs(docs):

    doc_embeddings = embed_text(docs)

    dimension = doc_embeddings.shape[1]
    index = faiss.IndexFlatIP(
        dimension
    )
    index.add(doc_embeddings)

    return index