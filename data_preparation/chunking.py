import json
import random
#QA
def verify_dataset_quality(json_file, sample_size=5):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    samples = random.sample(data, min(sample_size, len(data)))
    for i, s in enumerate(samples):
        print(f"--- Sample {i+1} ---")
        print(f"Q: {s['instruction']}")
        print(f"A: {s['output']}\n")


        #  (RAG CHUNKING)
def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap

    return chunks