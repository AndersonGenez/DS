import os

def obtenerRuta() :
    ruta = input ("Indique la ruta, sino se tomará la actual: ") 
    if (ruta=="") :
        ruta = rutaActual()
    return ruta

def rutaActual() :
    return os.getcwd()+"/"

def esArchivo(rutalCompleta) :
    return os.path.isfile (rutalCompleta)

def esRutaValida(rutaCompleta) :
    return os.path.isdir(rutaCompleta)