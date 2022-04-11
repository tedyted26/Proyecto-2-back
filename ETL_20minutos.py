# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import request as rq
import ssl
import datetime as dt
import re
import selenium

import os
from pathlib import Path
from Noticia import Noticia

def get20MinutosNews(categoria):
    #print(mainUrl)
    listaNoticias = []
    for paginas in range(1,3):
        #print(paginas)
        urlBase = "https://www.20minutos.es/busqueda/"
        urlIntermedio = "/?q="
        urlCola = "&sort_field=&category=&publishedAt%5Bfrom%5D=&publishedAt%5Buntil%5D="
        
        mainUrl = urlBase + str(paginas) + urlIntermedio + categoria + urlCola
    
        
        html = rq.urlopen(mainUrl, context=ssl.SSLContext()).read()
        #print(html)
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup)
        articulos = soup.findAll("article")
        #print(articulos[0])
        listaLinks = []
        
        for a in articulos:
            link = a.find("a")["href"]
            listaLinks.append(link)
        #print(listaLinks)
            
        for link in listaLinks:
            try:
                url = link
                htmlTemp = rq.urlopen(url, context=ssl.SSLContext()).read()
                soupPag = BeautifulSoup(htmlTemp, 'html.parser')
    
                titulo = soupPag.find("div", class_="title").text
                subtitulo = soupPag.find("div", class_="article-intro").text
                fecha = soupPag.find(class_="article-date").text
                tags = [t.text.strip() for t in soupPag.findAll(class_="tag")]
                textoTmp = soupPag.find(class_="article-text").text
                texto = re.sub("\s+", " ", textoTmp)
    
                date_regEx = re.compile(r'(\d+.\d+.\d+\s*-\s*\d*:\d*)')
                fecha = dt.datetime.strptime(date_regEx.search(fecha).group(), '%d.%m.%Y - %H:%M')
    
                n = Noticia(titulo, subtitulo, fecha, url, categoria, "20Minutos", tags, texto)
                listaNoticias.append(n)
            except Exception as e:
                print(e)
        #print(listaLinks)
    
    return listaNoticias

def guardarNoticias(listaN: list, ruta):
    fechaAnterior = ""
    for n in listaN:
        try:
            nuevaFecha = f"{n.fecha.year}-{n.fecha.month}-{n.fecha.day}"
            
            if(nuevaFecha != fechaAnterior):
                noticiasDiarias = 1
            else:
                noticiasDiarias = noticiasDiarias + 1
                
            nombreArchivo = n.categoria + "." + nuevaFecha + "." + str(noticiasDiarias).zfill(3) + ".txt"
            print(nombreArchivo)

            s = "\n#####\n"
            texto = f"{n.url}{s}" \
                    f"{n.periodico}{s}" \
                    f"{n.categoria}{s}" \
                    f"{n.fecha}{s}" \
                    f"{n.titulo}{s}" \
                    f"{n.subtitulo}{s}" \
                    f"{n.texto}{s}" \
                    f"{n.tags}" \
                # Path(ruta).mkdir(parents=True, exist_ok=True)
            cd = os.getcwd() + "/"+n.periodico

            if not os.path.exists(cd):
                os.mkdir(cd)
            cd2 = cd + ruta

            if not os.path.exists(cd2):
                os.mkdir(cd2)
            f = open(os.path.join(cd2, nombreArchivo), "w")
            f.write(texto)
            f.close()
            fechaAnterior = nuevaFecha
        except Exception as e:
            print(e)


def el20Minutos():
    
    busqueda = "ponferrada"
    
    noticias = get20MinutosNews(busqueda)
    guardarNoticias(noticias, ("/"+busqueda))
    '''
    print(noticias[1].periodico)
    print(noticias[1].fecha)
    print("\n")
    print(noticias[1].titulo)
    print("\n")
    print(noticias[1].subtitulo)
    print("\n")
    print(noticias[1].texto)
    '''
    
   
el20Minutos()

'''
mainUrl = "https://elpais.com/buscador/?q="
buscar = "barajas"
urlBuscador = mainUrl + buscar

urlElMundo = "https://ariadna.elmundo.es/buscador/archivo.html?q=barajas&b_avanzada="
'''