#External Imports

import re
import requests
from bs4 import BeautifulSoup
#import json

#Internal Imports
from Noticia import Noticia
from Guardado import guardarNoticias



def scraper_la_sexta(count_pages):
    lista_noticias = []
    fechaAnterior = ""
    url_base = "https://www.lasexta.com/"
    url_odio = "temas/delitos_de_odio-"
    #For para Scrape de las URL pagina por Pagina
    for paginas in range(1,count_pages): #Se empieza a partir de la segunda para facilitar la busqueda por url porque la 1 no tiene numero
        
        url = url_base + url_odio + str(paginas)
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            articulos = soup.findAll("article")
            urls = []
            
            print("###########################")
            print("Pagina: " +str(paginas+1))
            print("###########################")

            for articulo in articulos: 
                regex = 'link href="(.*?)"' 
                resultado_regex = re.search(regex, str(articulo))
                if resultado_regex != None:
                    urls.append(resultado_regex.group(1))

        except Exception as e:
            print(e)

        for i in range(0, len(urls)):
            try:
                noticia = requests.get(urls[i])
                print("NOTICIA: " + str(i))
                print("--------------------------")
                print(urls[i])
                print("--------------------------")

                #Imprimimos el contenido de la página
                soup_noticia = BeautifulSoup(noticia.content, 'html.parser')
                    
                regexTitulo = '<h1[\w\W]*?>(.*?)<\/h1>'
                regexAutor = '<div class="ue-c-article__byline-name">([\w\W]*?)<\/div>'
                regexFecha = '<time datetime="(.*?)T'
                regexEntradilla = '<p class="ue-c-article__standfirst">(.*?)<\/p>'
                regexCuerpo = '<p>(.*?)<\/p>'
                regexTags = 'tags-item"><a href=[\W\w]*?>(.*?)<'
            
                    
                titulo = re.search(regexTitulo, str(soup_noticia))
                titulo = titulo.group(1)
                titulo = re.sub(r'\<.*?\>', '', titulo)
                print(titulo)
                
                autor = re.search(regexAutor, str(soup_noticia))
                if autor != None:
                    autor = autor.group(1)
                    autor = re.sub(r'\<.*?\>', '', autor)
                    autor.replace('\n', '')
                    autor.rstrip("\n")
                else:
                    autor = ""
                print(autor)
                
                fecha = re.search(regexFecha, str(soup_noticia))
                if fecha != None:
                    fecha = fecha.group(1)
                else:
                    fecha = ""
                
                entradilla = re.search(regexEntradilla, str(soup_noticia))
                if entradilla != None:
                    entradilla = entradilla.group(1)
                    entradilla = re.sub(r'\<.*?\>', '', entradilla)
                else:
                    entradilla = ""
                print (entradilla)
                
                parrafos = re.findall(regexCuerpo, str(soup_noticia))
                if parrafos == None:
                    parrafos = ""
                else:
                    cuerpo = ""
                    for parrafo in parrafos:
                        if cuerpo == "":
                            cuerpo = parrafo
                        else:
                            cuerpo = cuerpo + ' ' + parrafo
                    cuerpo = re.sub(r'\<.*?\>', '', cuerpo)
                print(cuerpo)
                
                tags = re.findall(regexTags, str(soup_noticia))
                if tags == None:
                    etiquetas = ""
                else:
                    etiquetas = ""
                    for tag in tags:
                        if etiquetas == "":
                            etiquetas = tag
                        else:
                            etiquetas = etiquetas + ', ' + tag
                    etiquetas = re.sub(r'\<.*?\>', '', etiquetas)
                print(etiquetas)   
                
                if fecha != "":                    
                    if(fecha != fechaAnterior):
                        noticiasDiarias = 1
                    else:
                        noticiasDiarias = noticiasDiarias + 1
                    noticia = Noticia(titulo, entradilla, fecha, url, "ODIO", "La Sexta", etiquetas, cuerpo )
                    lista_noticias.append(noticia)
                    
                
                print("\n")
            except Exception as e:
                print(e)
            
    return lista_noticias
            



if __name__ == "__main__":
    lista_noticias = scraper_la_sexta(5) 
    guardarNoticias(lista_noticias, ("/NoticiasOdio"))