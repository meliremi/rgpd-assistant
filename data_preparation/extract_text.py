import pdfplumber
import os

from data_preparation.chunking import chunk_text
from rag.embeddings import embed_chunks 

def run_extraction(pdf_path=r"data_preparation\RGPD.pdf"):
    documents = []

    if not os.path.exists(pdf_path):
        print(f"Erreur : Le fichier {pdf_path} n'existe pas.")
        return documents

    if not pdf_path.endswith(".pdf"):
        print("Erreur : Le fichier fourni n'est pas un PDF.")
        return documents

    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""

            for page in pdf.pages:
                text += page.extract_text() or ""

            documents.append({
                "source": os.path.basename(pdf_path),
                "content": text
            })

        print(f"Extraction terminée pour : {os.path.basename(pdf_path)}")

    except Exception as e:
        print(f"Erreur lors de l'extraction : {e}")

    return documents


# =========================
# TEST PIPELINE RAG
# =========================

docs = run_extraction()

if docs:
    text = docs[0]["content"]

    # 1. CHUNKING
    chunks = chunk_text(text)

    # 2. EMBEDDINGS
    embeddings = embed_chunks(chunks)

    # 3. OUTPUT TEST
    print("nb chunks:", len(chunks))
    print("nb embeddings:", len(embeddings))
    print("dimension:", len(embeddings[0]))

    print("\n--- exemple chunk ---")
    print(chunks[0])