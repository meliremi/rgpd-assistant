from sentence_transformers import SentenceTransformer

# modèle léger et rapide (bon choix pour projet M2)
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_chunks(chunks):
    """
    Transforme une liste de chunks texte en embeddings vectoriels
    """
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings