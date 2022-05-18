from archivo import crearArchivo
import webbrowser
import os

ruta = os.getcwd()+"/"
archivo = crearArchivo(ruta)

pagina = open(archivo, 'w')

html = '<!DOCTYPE html><html lang=en><meta charset=UTF-8><meta content="IE=edge"http-equiv=X-UA-Compatible><meta content="width=device-width,initial-scale=1"name=viewport><title>Programación 2</title><h1>Programación 2</h1><ul><li>Condicionales<li>Bucles<li>Listas<li>Funciones<li></ul>'

pagina.write(html)
pagina.close()

webbrowser.open(os.getcwd()+"/"+archivo)