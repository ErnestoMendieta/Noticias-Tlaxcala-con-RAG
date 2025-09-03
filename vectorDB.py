import chromadb
import pandas as pd

client = chromadb.Client()

df = pd.read_csv("data.csv")

# obtener embeddings
embList = df["embedding"].tolist()

# obtener noticias y descripciones para generar los documentos para la bd 
noticia = pd.concat([df["Titulo"], df["descripcion"]], axis=1)
documentos = noticia.apply(lambda x: x["Titulo"] + " " + x["descripcion"], axis=1).tolist()

# obtener url y el tipo de noticia para los metadatos 
metadatos = pd.concat([df["tipo"], df["url"]], axis=1)
# orientar el mapa correctamente
mdList = metadatos.to_dict(orient="records")

# creacion de ids
idList = ["n"+str(x) for x in range(len(df))]
# print("Tipo de metadatos:", type(metadatos))
# print("Tipo de md:", type(md))
# print("Ejemplo de metadatos:", metadatos.head(2) if hasattr(metadatos, 'head') else metadatos[:2])
# print("Ejemplo de md:", md[:2] if isinstance(md, list) else md)
collection = client.get_or_create_collection(name="noticias",  embedding_function=None)

collection.upsert(
    ids= idList,
    embeddings = embList,
    documents= documentos,
    metadatas= mdList
)

# results = collection.query(
#     query_texts="Saludos cordiales",
#     n_results=2
# )

# print(results)