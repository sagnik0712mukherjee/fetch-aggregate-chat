from sentence_transformers import SentenceTransformer
from config.settings import embedding_model
import faiss

model = SentenceTransformer(embedding_model)


def embed_text(texts):

    embedded_text = model.encode(texts, convert_to_numpy=True)
    faiss.normalize_L2(embedded_text)

    return embedded_text
