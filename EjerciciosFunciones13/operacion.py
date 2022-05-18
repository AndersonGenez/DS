from ruta import obtenerRuta, rutaActual, esRutaValida
from acciones import eliminarItem
from carpeta import crearCarpeta
from archivo import crearArchivo
# from main import init


def crear() :
    crearDic = { 'a': crearArchivo, 'c': crearCarpeta }
    ruta = obtenerRuta()
    #comprobar si la ruta existe 
    if (esRutaValida(ruta)) :
        tipo = input("Indique el tipo a=archivo y c=carpeta: ") 

        if (tipo == "a" or tipo == "c"):
            crearDic[tipo](ruta)

        else: return False

def eliminar() :
    ruta = input ("Indique la ruta, sino se tomará la actual: ") 

    if (ruta == ""):
        ruta = rutaActual()
    item = input ("Indique el nombre de la carpeta o archivo a eliminar") 

    eliminacion = eliminarItem(ruta, item)
    if (eliminacion == False):
        return False