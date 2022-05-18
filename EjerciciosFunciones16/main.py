'''
16-Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la primera
letra de cada palabra a mayúscula y las demás letras a minúscula, dejando
inalterados los demás caracteres. Precondición: el separador de palabras es el
espacio: " ". Agregar doctests con suficientes casos de prueba para validar que la
función retorna el valor esperado ante distintos argumentos.
'''

from modulo16 import titulo

arg1 = '-Lorem- ipsum dolor sit amet consectetur adipisicing elit. Voluptatum cum quisquam adipisci tempore'
arg2 = 'LISTA DE FECHAS DESTACADAS: Fecha 1- 460 a.C. Atenas se vuelve democrática. Fecha 2- 323 a.C.'
arg3 = 'Averiguar y sacar CUIL o CUIT online con DNI (anses - afip) - Mi Cuil'
arg4 = 'https://docs.python.org/ https://www.google.com/'

print(titulo(arg1))
print(titulo(arg2))
print(titulo(arg3))
print(titulo(arg4))