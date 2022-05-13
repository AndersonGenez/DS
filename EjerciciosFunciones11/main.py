'''
11- Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera
que las palabras están separadas por uno o más espacios. También podría haber espacios
al principio o al final del string pasado por parámetro.
'''

from modulo import obtenerLenUltimaPalabra

texto = input('Ingrese una oracion: ')
resultado = obtenerLenUltimaPalabra(texto)

print(resultado)