import pdfplumber
import os

def run_extraction(pdf_path=r"C:\Users\HP\Desktop\projet RGPD selma\rgpd-assistant\data_preparation\RGPD.pdf"):
    """
    Extrait le texte du fichier PDF spécifié.
    Utilise pdfplumber pour lire le contenu du PDF.
    """

    documents = []

    # Vérifie si le fichier existe
    if not os.path.exists(pdf_path):
        print(f"Erreur : Le fichier {pdf_path} n'existe pas.")
        return documents

    # Vérifie que c'est bien un PDF
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


# Exemple d'utilisation
docs = run_extraction()

if docs:
    print(docs[0]["content"][:1000])