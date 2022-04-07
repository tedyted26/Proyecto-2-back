from bs4 import BeautifulSoup
from urllib import request as rq
from Noticia import Noticia 

import ssl


categoria = "badajoz"
urlbase = "https://www.abc.es/hemeroteca/noticia/"
url = urlbase + categoria
html = rq.urlopen(url, context=ssl.SSLContext()).read()
soup = BeautifulSoup(html, 'html.parser')

resultados = soup.find(id="results-content")
 

for li in resultados.findAll("li"):
    link = li.find("a")["href"]

    html_noticia = rq.urlopen(link, context=ssl.SSLContext()).read()
    soupTmp = BeautifulSoup(html_noticia, 'html.parser')

    encabezado = soupTmp.find(class_="encabezado-articulo")
    titulo = encabezado.find(class_="titular").text
    subtitulo = encabezado.find(class_="subtitulo").text

    cuerpo = soupTmp.find(class_="cuerpo-texto")
    fecha = cuerpo.find(class_="fecha").find("time")["datetime"]
    texto = " ".join([x.text for x in cuerpo.findAll("p")])
    tags = [x.text for x in cuerpo.find(class_="modulo temas").findAll("li")]
    bloqueCOM = cuerpo.find(class_="comentarios")
    listaCOM = cuerpo.findAll(class_="gig-comment-body")
    #Los comentarios no funcionan porque se carga dinamicamente
    #comentarios = [x.text for x in cuerpo.findAll(class_="gig-comment-body")]
    

    noticia = Noticia(titulo, subtitulo, fecha, link, categoria, "ABC", tags, texto)
    print(titulo,link, "\n----\n")

