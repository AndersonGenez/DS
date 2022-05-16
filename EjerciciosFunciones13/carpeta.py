import os

def crearCarpeta(ruta) :
    carpeta=input ("Indique el nombre de la carpeta" )
    os.mkdir (ruta+carpeta)
    print("Carpeta ", carpeta, "creada con exito")

def eliminarCarpeta (rutaCompleta) :
    os.rmdir (rutaCompleta)
