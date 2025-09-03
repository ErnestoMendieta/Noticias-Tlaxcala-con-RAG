import requests
import json
from bs4 import BeautifulSoup
import re
import unicodedata


def obtainArticle(url):
    req = requests.get(url)
    archivo = "html.txt"
    
    soup = BeautifulSoup(req.content,"html.parser")
    content = soup.find_all("div", class_="group-grid-article_article___ZsfO")
    # p= content.find_all("p") 
    # for i in content:
    #     # if (i.p):
    #     #     print(i.p)
    #     # else:
    #     print(i,)

    p_tags = soup.select("div.group-grid-article_article___ZsfO p")
    with open(archivo, 'w') as f:
    
        f.writelines(str(content))
    # for p in p_tags:
    #     print(p.get_text())
        # print("+-+-+-+-+0", i)
        

obtainArticle("https://oem.com.mx/elsoldetlaxcala/policiaca/hallan-seis-cabezas-humanas-en-ixtacuixtla-un-hecho-sin-precedentes-en-tlaxcala-25290630")