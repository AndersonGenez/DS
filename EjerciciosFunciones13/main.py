'''
13- Realizar un programa usando funciones que permita administrar carpetas y archivos. De
acuerdo a la función seleccionada llamar a la función correspondiente.
''' 

import os
from modulos import crearCarpeta

def init() :
    print("**** ADMINISTRAR ARCHIVOS ****")
    opcion=input ("Selecciona una opción c=crear y e=eliminar ") 
    if (opcion=="c"):
        ruta= input ("Indique la ruta, sino se tomará la actual: ") 
        if (ruta==""): ruta=os.getcwd()+"/"
        #comprobar si la ruta existe 
        if (os.path.isdir (ruta)) :
            tipo = input ("Indique el tipo a=archivo y c=carpeta: ") 
            if (tipo=="a"):
                archivo=input ("Indique el nombre del Archivo: ")
                #Crear el archivo
                manejador=open (ruta+archivo, "W")
                manejador.close()
                print("Archivo", archivo, "creado con exito") 
            elif (tipo=="c") :
                crearCarpeta()
            else: init()
        elif (opcion=="e"):
            ruta= input ("Indique la ruta, sino se tomará la actual: ") 
            if (ruta==""): ruta=os.getowd()+"/"
            eliminar = input ("Indique el nombre de la carpeta o archivo a eliminar") 
            if (os.path.isfile (ruta+eliminar)):
                os.remove (ruta+eliminar)
                print("Archivo ", eliminar, "eliminado con éxito")
            elif (os.path.isdir (ruta+eliminar)):
                os.rmdir (ruta+eliminar)
            else:
                init() 
    else: init()

init()