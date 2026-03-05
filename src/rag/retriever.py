import faiss
from sentence_transformers import SentenceTransformer
from config.settings import embedding_model

model = SentenceTransformer(embedding_model)


def retrieve_results(user_query, docs, index, top_k=3):

    embedded_query = model.encode([user_query], convert_to_numpy=True)
    faiss.normalize_L2(embedded_query)

    _scores, indices = index.search(embedded_query, top_k)

    print(f"INDICES\n{indices}\n\n")

    results = [docs[i] for i in indices[0] if i != -1]
    return results
