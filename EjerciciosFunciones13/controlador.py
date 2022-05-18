'''
13- Realizar un programa usando funciones que permita administrar carpetas y archivos. De
acuerdo a la función seleccionada llamar a la función correspondiente.
''' 

from operacion import crear, eliminar

operacion = { 'c': crear, 'e': eliminar }

def init() :
    print("**** ADMINISTRAR ARCHIVOS ****")
    opcion=input ("Selecciona una opción c=crear y e=eliminar ") 

    if (opcion == 'c' or opcion == 'e') :
        res = operacion[opcion]()
        if res == False :
            return False
        
    else:
        return False
