import json

SYSTEM_PROMPT = """Tu es un expert en création de datasets pour LLM. 
A partir d'un passage RGPD, génère exactement 3 paires Q/R. 
Questions variées factuelles, analytiques, compréhension.
Réponses précises, complètes, basées uniquement sur le texte.
Retourne UNIQUEMENT un JSON valide.""" [cite: 58, 59, 60, 61, 62]

def generate_qa_pairs(client, chunk_text):
    prompt = f"{SYSTEM_PROMPT}\n\nTexte source: {chunk_text}"
    # Simulation de l'appel API (Groq/OpenAI)
    response = client.chat.completions.create(
        model="gpt-4", # ou Mixtral via Groq
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(response.choices[0].message.content)