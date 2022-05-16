'''
13- Realizar un programa usando funciones que permita administrar carpetas y archivos. De
acuerdo a la función seleccionada llamar a la función correspondiente.
''' 

from ruta import obtenerRuta, rutaActual, esRutaValida
from acciones import eliminarItem
from carpeta import crearCarpeta
from archivo import crearArchivo

crear = { 'a': crearArchivo, 'c': crearCarpeta }

def init() :
    print("**** ADMINISTRAR ARCHIVOS ****")
    opcion=input ("Selecciona una opción c=crear y e=eliminar ") 
    if (opcion=="c"):
        ruta = obtenerRuta()
        #comprobar si la ruta existe 
        if (esRutaValida(ruta)) :
            tipo = input ("Indique el tipo a=archivo y c=carpeta: ") 

            if (tipo == "a" or tipo == "c"):
                crear[tipo](ruta)

            else: init()
    elif (opcion=="e"):
        ruta = input ("Indique la ruta, sino se tomará la actual: ") 

        if (ruta == ""):
            ruta = rutaActual()
        item = input ("Indique el nombre de la carpeta o archivo a eliminar") 

        eliminacion = eliminarItem(ruta, item)
        if (eliminacion == False):
            init() 
    else: init()

init()