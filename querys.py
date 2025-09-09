import chromadb
import custEmb

client = chromadb.PersistentClient(path="db")
gemini_emb = custEmb.GeminiEmbeddingFunction()
collection = client.get_collection(name="noticias", embedding_function=gemini_emb)
# Agrega esto antes de tu query
print("Conteo de documentos:", collection.count())
print("Nombres de colecciones:", client.list_collections())

results = collection.query(
    query_texts="Chiautempan",
    n_results=2
)

print(results)
# results = collection.query(query_texts="Tlaxcala", n_results=2)
print("Estructura del resultado:")
for key, value in results.items():
    print(f"{key}: {type(value)}")