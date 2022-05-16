import os

def crearArchivo (ruta) :
    archivo=input ("Indique el nombre del Archivo: ")
    #Crear el archivo
    manejador=open (ruta+archivo, "W")
    manejador.close()
    print("Archivo", archivo, "creado con exito") 

def eliminarArchivo (ruta, archivo) :
    os.remove (ruta+archivo)
    print("Archivo ", archivo, "eliminado con éxito")