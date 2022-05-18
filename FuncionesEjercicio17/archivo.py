'''
17-Usar la función webbroser para mostrar una página html que tenga el título
Programación 2 y muestre una lista desordenada con los siguientes ítems:
Condicionales
Bucles
Listas
Funciones
Agregar enlace para ingresa a cada una de las opciones
'''
import os

def crearArchivo (ruta) :
    archivo=input ("Indique el nombre del Archivo: ")
    #Crear el archivo
    archivo += '.html'
    manejador=open (ruta+archivo, "w")
    manejador.close()
    print("Archivo", archivo, "creado con exito")
    return archivo
