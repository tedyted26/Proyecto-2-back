from bs4 import BeautifulSoup
from urllib import request as rq
from Noticia import Noticia
# pip install selenium
# pip install webdriver_manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import ssl

driver = webdriver.Chrome(ChromeDriverManager().install())

categoria = "salamanca"
urlbase = "https://stories.lavanguardia.com/search?q="
url = urlbase + categoria
html = None

# ver que hacer con los resultados de la busqueda que no llevan a ninguna parte
try:
    html = rq.urlopen(url, context=ssl.SSLContext()).read()
except:
    print("Pagina no encontrada")

if html != None:
    resultados = []
    soup = BeautifulSoup(html, 'html.parser')
    # recoger todos los <article class="result"
    resultados.extend(soup.find_all(class_="result"))

    # para paginación
    # pagina 1: https://stories.lavanguardia.com/search?q=salamanca
    # pagina 2: https://stories.lavanguardia.com/search?q=salamanca&author=&category=&section=&startDate=&endDate=&sort=&page=2
    # no funciona si uso el enlace de la pag 2 para la 1

    filters = "&author=&category=&section=&startDate=&endDate=&sort=&page="
    fin_pag = False
    page = 2
    while fin_pag == False:
        url_pag = url + filters + str(page)
        html_pag = None

        try:
            html_pag = rq.urlopen(url_pag, context=ssl.SSLContext()).read()
        except:
            fin_pag = True

        if html_pag != None:
            soup_pag = BeautifulSoup(html_pag, 'html.parser')
            resultados.extend(soup_pag.find_all(class_="result"))
            page = page + 1

    noticias = []

    # dentro de las noticia
    for article in resultados:
        url_art = article.find("a")["href"]
        # esta url es solo de prueba
        url_art = "https://www.lavanguardia.com/internacional/20220408/8185819/rusia-excluida-consejo-derechos-humanos-onu.html"
        html_art = rq.urlopen(url_art, context=ssl.SSLContext()).read()
        soup_art = BeautifulSoup(html_art, 'html.parser')

        titulo = soup_art.find(class_="title").text

        subtitulos = soup_art.find_all(class_="epigraph")
        subtitulo = ""
        for sub in subtitulos:
            subtitulo = subtitulo + sub.text

        fecha = soup_art.find("time")["datetime"]

        categoria = soup_art.find(class_="supra-title").text

        periodico = "La Vanguardia"

        tags = ""

        texto_entero = soup_art.find(class_="article-modules").find_all("p")
        texto = ""
        for p in texto_entero:
            texto = texto + p.text

        driver.get(url_art)

        #cart = driver.find_element_by_class_name("spotim-open")
        #cart.click()
        #modal_comentarios = soup_art.find(class_="comments-modal") # spcv_messages-list
        #print(modal_comentarios.prettify())
        #ul_comentarios = modal_comentarios.find("ul")
        #lista_comentarios = ul_comentarios.find_all(class_="spcv_list-item")


