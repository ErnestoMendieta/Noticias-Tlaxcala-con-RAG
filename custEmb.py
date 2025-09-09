from google import genai
from chromadb.api.types import EmbeddingFunction, Documents, Embeddings
import numpy as np

class GeminiEmbeddingFunction(EmbeddingFunction[Documents]):
    def __init__(self, model_name: str = "models/embedding-001", api_key: str = None):
        
        self.model_name = model_name

    @staticmethod

    def __call__(self, input: Documents) -> Embeddings:
        embeddings = []
        client = genai.Client()
        for text in input:
            result = client.models.embed_content(
                model=self.model_name,
                contents=text
            )
            vector = [emb.values for emb in result.embeddings]
            # print(vector[0])
            # print(f"Tipo de vector: {type(vector)}")
            # print(f"Longitud de vector: {len(vector)}")
            # print(f"Tipo del primer elemento: {type(vector[0]) if vector else 'vector vacío'}")
            # print(f"¿Es una lista de listas?: {isinstance(vector[0], list) if vector else 'No aplica'}")
            embeddings.append(vector[0])
        return embeddings
