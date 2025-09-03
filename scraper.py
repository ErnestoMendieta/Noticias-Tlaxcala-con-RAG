import requests
import json
from bs4 import BeautifulSoup
import re
import unicodedata

def normalize(texto): 
    # Quita acentos usando NFD
    texto = unicodedata.normalize("NFD", texto)
    # Elimina caracteres diacríticos (acentos, tildes, diéresis)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    # Reemplaza ñ → n
    texto = texto.replace("ñ", "n").replace("Ñ", "N")
    return texto

req = requests.get("https://oem.com.mx/elsoldetlaxcala/")
archivo = "info.json"
# instancia de beautifulSoup
# print(req.text)

soup = BeautifulSoup(req.content, "html.parser")
content= soup.find_all("article", class_="Teaser_teaser__Lkcni")
# print(soup["class"])

info = []

for i in content:
   
    tipo =i.find("div", class_="Typography_text-s__wu_cm")
    
    if(tipo):
        tipoNot = tipo.string
    else:
        tipoNot="no especificado"
        
    img = i.find("img")
    imagen = img["src"]
    rawTitle= i.h3.string
    title = normalize(rawTitle)
    # descripcion = i.p.string if (i.p.string) == True else "no descripcion"
    try:
        raw = i.p.string
        descripcion = normalize(raw)
    except:
        descripcion = "no descripcion"
    
    ligaCruda = i.a["href"]
    liga = str("https://oem.com.mx"+ligaCruda)
    # print(liga)   
    
    elemento = {"Titulo": title, "imagen": imagen, "tipo": tipoNot, "descripcion": descripcion, "url": liga}
    # print(texto)
    # print(imagen)
    info.append(elemento)
    
    
with open(archivo, 'w') as f:
    
    json.dump(info,f,indent=5,ensure_ascii=False) 
# print(json_string)
# if(content):
#     for p in content.findAll("p"):
#         # print(p.text.strip())




