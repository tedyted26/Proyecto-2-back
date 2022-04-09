from bs4 import BeautifulSoup
from urllib import request as rq
from Noticia import Noticia 

import ssl

# ver que hacer con los resultados de la busqueda que no llevan a ninguna parte

# recoger todos los <article class="result"

# para paginación
# pagina 1: https://stories.lavanguardia.com/search?q=salamanca
# pagina 2: https://stories.lavanguardia.com/search?q=salamanca&author=&category=&section=&startDate=&endDate=&sort=&page=2
# no funciona si uso el enlace de la pag 2 para la 1

# dentro de la noticia
# <h1 class="title"
# <h2 class="epigraph"
# <time datetime="2021-01-10T11:29:12+01:00" class="created">10/01/2021 11:29</time>
# url pillarla de antes
# <h2 class="supra-title" para la categoría?
# periodico = la vanguardia
# no hay tags
# para ver los comentarios usar selenium en: <div class="spotim-open comments-bbd14976-532c-11eb-acb3-c65f349e9d3e-20210110112042">Mostrar comentarios</div> Comprobar que los numeros estan bien
# dentro de <div class="article-modules" pillar todos los <p> (texto)

