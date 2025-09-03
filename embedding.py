import json
from google import genai
from google.genai import types
import pandas as pd


archivo = "info.json"

with open(archivo, 'r') as file:
    data = json.load(file)


# titulos = [item["Titulo"] for item in data]
# descripciones = [item["descripcion"] for item in data]

df = pd.DataFrame(data)

strings = []
for item in data:
    titulo = item["Titulo"]
    descripcion = item["descripcion"]
    if descripcion!= "no descripcion":
        string = titulo + " " + descripcion
    else:
        string = titulo
    strings.append(string)
zsss
# strings=["hola como estas", "saludos amigo mio", "adios amiga", "nos vemos luego"]

client = genai.Client()
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=strings)

vector = [emb.values for emb in result.embeddings]
df["embedding"] = vector
# Save the DataFrame to a CSV file
df.to_csv('data.csv', index=False)
# print(df)