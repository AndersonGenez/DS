from ruta import esArchivo, esRutaValida
from archivo import eliminarArchivo
from carpeta import eliminarCarpeta

def eliminarItem(ruta, eliminar) :
    if (esArchivo(ruta+eliminar)) :
        eliminarArchivo(ruta, eliminar)

    elif (esRutaValida(ruta+eliminar)) :
        eliminarCarpeta(ruta+eliminar)

    else:
        return False