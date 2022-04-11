# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 17:48:32 2022

@author: Yago
"""
import os
#from pathlib import Path

class Guardado:
    
    def guardarNoticias(self, listaN: list, ruta):
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